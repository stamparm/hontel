# HonTel [![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/stamparm/hontel#license-mit)

**HonTel** is a Honeypot for Telnet service. Basically, it is a Python v2.x application emulating the service inside the [chroot](https://help.ubuntu.com/community/BasicChroot) environment. Originally it has been designed to be run inside the Ubuntu environment, though it could be easily adapted to run inside any Linux environment.

## Documentation:

Setting the environment and running the application requires intermmediate Linux administration knowledge. The whole deployment process can be found "step-by-step" inside the [deploy.txt](https://github.com/stamparm/hontel/blob/master/deploy.txt) file. Configuration settings can be found and modified inside the [hontel.py](https://github.com/stamparm/hontel/blob/master/hontel.py) itself. For example, authentication credentials can be changed from default `root:123456` to some arbitrary values (options `AUTH_USERNAME` and `AUTH_PASSWORD`), custom *Welcome* message can be changed from default <blank> (option `WELCOME`), custom *hostname* (option `FAKE_HOSTNAME`), architecture (option `FAKE_ARCHITECTURE`), location of log file (inside the chroot environment) containing all telnet commands (option `LOG_PATH`), location of downloaded binary files dropped by connected users (option `SAMPLES_DIR`), etc.

Note: Some botnets tend to delete the files from compromised hosts (e.g. `/bin/bash`) in order to harden itself from potential attempts of cleaning and/or attempts of installation coming from other botnets. In such cases either the whole chroot environment has to be reinstalled or host directory where the chroot directory resides (e.g. `/srv/chroot/`) should be recovered from the previously stored backup.

![hontel](http://i.imgur.com/zLCMLML.png)

## License

This software is provided under under a MIT License. See the accompanying [LICENSE](https://github.com/stamparm/hontel/blob/master/LICENSE) file for more information.
