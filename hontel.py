#!/usr/bin/env python

# Copyright (c) 2015 Miroslav Stampar (@stamparm)
# See the file 'LICENSE' for copying permission

import fcntl
import os
import re
import signal
import SocketServer
import stat
import subprocess
import threading
import time

try:
    from telnetsrv.threaded import TelnetHandler, command
except ImportError:
    exit("[!] please install telnetsrv (e.g. 'pip install telnetsrv')")

AUTH_USERNAME = "root"
AUTH_PASSWORD = "123456"
WELCOME = None
LOG_PATH = "/var/log/%s.log" % os.path.split(__file__)[-1].split('.')[0]
READ_SIZE = 1024
CHECK_CHROOT = True
THREAD_DATA = threading.local()
LOG_FILE_PERMISSIONS = stat.S_IREAD | stat.S_IWRITE | stat.S_IRGRP | stat.S_IROTH
LOG_HANDLE_FLAGS = os.O_APPEND | os.O_CREAT | os.O_WRONLY
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
USE_BUSYBOX = True
LISTEN_ADDRESS = "0.0.0.0"
LISTEN_PORT = 23

if CHECK_CHROOT:
    chrooted = False
    try:
        output = subprocess.check_output("ls -di /", shell=True)
        if int(output.split()[0]) != 2:
            chrooted = True
    except:
        pass
    finally:
        if not chrooted:
            exit("[!] run inside the chroot environment")

if USE_BUSYBOX:
    try:
        SHELL = "/bin/busybox sh"

        _ = subprocess.check_output("/bin/busybox")
        _ = _.split("\n")[0]
        match = re.search(r".+\)", _)
        if match:
            _ = "%s built-in shell (ash)" % match.group(0)
        WELCOME = "\n%s\nEnter 'help' for a list of built-in commands.\n" % _
    except OSError:
        exit("[!] please install busybox (e.g. 'apt-get install busybox')")
else:
    SHELL = "/bin/bash"

class HoneyTelnetHandler(TelnetHandler):
    WELCOME = WELCOME
    PROMPT = "# "

    authNeedUser = AUTH_USERNAME is not None
    authNeedPass = AUTH_PASSWORD is not None

    def _readline_echo(self, char, echo):
        if "^C ABORT" in char:
            char = "^C\n"
            os.killpg(self.process.pid, signal.SIGINT)
        if self._readline_do_echo(echo):
            self.write(char)

    def _log(self, logtype, msg=None):
        line = '[%s] [%s:%s] %s%s\n' % (time.strftime(TIME_FORMAT, time.localtime(time.time())), self.client_address[0], self.client_address[1], logtype, ": %s" % msg if msg is not None else "")
        os.write(self._getLogHandle(), line)

    def _getLogHandle(self):
        if LOG_PATH != getattr(THREAD_DATA, "logPath", None):
            if not os.path.exists(LOG_PATH):
                open(LOG_PATH, "w+").close()
                os.chmod(LOG_PATH, LOG_FILE_PERMISSIONS)
            THREAD_DATA.logPath = LOG_PATH
            THREAD_DATA.logHandle = os.open(THREAD_DATA.logPath, LOG_HANDLE_FLAGS)
        return THREAD_DATA.logHandle

    def _processRead(self):
        result = ""
        while self.process.poll() is None:
            try:
                buf = os.read(self.process.stdout.fileno(), READ_SIZE)
                buf = re.sub(r"%s: line \d+: " % SHELL, "", buf)
                result += buf
            except OSError:
                break
        return result

    def handleException(self, exc_type, exc_param, exc_tb):
        return False

    def session_start(self):
        self._log("SESSION_START")
        self.process = subprocess.Popen(SHELL, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, preexec_fn=os.setsid)

        flags = fcntl.fcntl(self.process.stdout, fcntl.F_GETFL)
        fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    def session_end(self):
        self._log("SESSION_END")

    def handle(self):
        if not self.authentication_ok():
            return
        if self.DOECHO and self.WELCOME:
            self.writeline(self.WELCOME)

        self.session_start()

        while self.RUNSHELL and self.process.poll() is None:
            line = self.input_reader(self, self.readline(prompt=self.PROMPT).strip())
            raw = line.raw
            cmd = line.cmd
            params = line.params

            self._log("CMD", raw)

            if self.COMMANDS.has_key(cmd):
                try:
                    self.COMMANDS[cmd](params)
                    continue
                except:
                    pass

            try:
                self.process.stdin.write(raw.strip() + "\n")
            except IOError, ex:
                raise
            finally:
                time.sleep(0.1)

            self.write(self._processRead())

    def authCallback(self, username, password):
        if username is not None and password is not None:
            self._log("AUTH", "%s:%s" % (username, password))

        if not(username == AUTH_USERNAME and password == AUTH_PASSWORD):
            raise Exception("[x] wrong credentials ('%s':'%s')" % (username, password))

class TelnetServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

server = TelnetServer((LISTEN_ADDRESS, LISTEN_PORT), HoneyTelnetHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    os._exit(1)
