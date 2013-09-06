-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Format: 1.0
Source: tor
Binary: tor, tor-dbg, tor-geoipdb
Architecture: any all
Version: 0.2.4.17-rc-1~d70.wheezy+1.1raspi0
Maintainer: Peter Palfrader <weasel@debian.org>
Homepage: https://www.torproject.org/
Standards-Version: 3.9.4
Vcs-Browser: https://gitweb.torproject.org/debian/tor.git
Vcs-Git: https://git.torproject.org/debian/tor.git
Build-Depends: debhelper (>= 8.1.0~), quilt, libssl-dev, zlib1g-dev, libevent-dev (>= 1.1), binutils (>= 2.14.90.0.7), hardening-includes, asciidoc (>= 8.2), docbook-xml, docbook-xsl, xmlto, dh-apparmor
Build-Conflicts: libnacl-dev
Package-List: 
 tor deb net optional
 tor-dbg deb debug extra
 tor-geoipdb deb net extra
Checksums-Sha1: 
 ed19e93188d620e1a5bca0e6c243ef5941490c05 2825527 tor_0.2.4.17-rc.orig.tar.gz
 01ec3762f5b399c89253fd513a87e20371295013 33700 tor_0.2.4.17-rc-1~d70.wheezy+1.1raspi0.diff.gz
Checksums-Sha256: 
 9d143b950a1c920e455bb41f2773e2bee8818e4a81aa9b1877db47d643b95d65 2825527 tor_0.2.4.17-rc.orig.tar.gz
 d9e55e9f98781a83fa6bd519a12bae04ec8cf167da5b3dd55d0b941a7bfd695d 33700 tor_0.2.4.17-rc-1~d70.wheezy+1.1raspi0.diff.gz
Files: 
 2cdfb8dcc3306a43cf465a858bf97b2d 2825527 tor_0.2.4.17-rc.orig.tar.gz
 3ee564e0c4efd794bb2bff0326dd1537 33700 tor_0.2.4.17-rc-1~d70.wheezy+1.1raspi0.diff.gz

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.12 (GNU/Linux)

iQEcBAEBAgAGBQJSKkeDAAoJED/jpRoe7/uj2S8H/jISG0LgBfI4OHKeNyNLWs7d
VY3QpQWRKVRZ5tRO7eXNU/wM7o/vUCtWxrj2bieNHs0VrnMwxHav5/zeGrq/Pduk
oiRAo7x5JA4+CVUOjKFoUkUOMD6I97zbStCvwOKNUbgYS0E4JAkGcZdYITKHdoh6
5mWQZTcepEyf6FfLeC4x0ZK4ZmmImBhXZw1vgKy11z9Ds2yKtWmerYDVhR67RmXE
FmpST+O4wAHpfyrqxaRI/xLTqW/ufDwS7yvosNK3MFnc0dilbZMlaCpOcNxSTf2N
tND5YhT5jn7ET8eE5HufmmNIOCIUp8bS1qiqiT3HhughcPMcHYSsIvJrU3+D+A0=
=lsEf
-----END PGP SIGNATURE-----
