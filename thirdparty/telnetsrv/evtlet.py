#!/usr/bin/python
# Telnet handler concrete class using green threads with eventlet

import eventlet

from telnetsrvlib import TelnetHandlerBase, command

class TelnetHandler(TelnetHandlerBase):
    "A telnet server handler using Gevent"
    def __init__(self, request, client_address, server):
        # Create a green queue for input handling
        self.cookedq = eventlet.queue.Queue()
        # Call the base class init method
        TelnetHandlerBase.__init__(self, request, client_address, server)

    def setup(self):
        '''Called after instantiation'''
        TelnetHandlerBase.setup(self)
        # Spawn a greenlet to handle socket input
        self.greenlet_ic = eventlet.spawn(self.inputcooker)
        # Note that inputcooker exits on EOF

        # Sleep for 0.5 second to allow options negotiation
        eventlet.sleep(0.5)

    def finish(self):
        '''Called as the session is ending'''
        TelnetHandlerBase.finish(self)
        # Ensure the greenlet is dead
        self.greenlet_ic.kill()


    # -- Green input handling functions --

    def getc(self, block=True):
        """Return one character from the input queue"""
        try:
            return self.cookedq.get(block)
        except eventlet.queue.Empty:
            return ''

    def inputcooker_socket_ready(self):
        """Indicate that the socket is ready to be read"""
        return eventlet.select.select(
            [self.sock.fileno()],
            [],
            [],
            0
        ) != ([], [], [])

    def inputcooker_store_queue(self, char):
        """Put the cooked data in the input queue (no locking needed)"""
        if type(char) in [type(()), type([]), type("")]:
            for v in char:
                self.cookedq.put(v)
        else:
            self.cookedq.put(char)

