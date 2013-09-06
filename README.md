cipollini
=========

Debian package selection (including scripts and extras) for a plug-in-and-forget Tor relay on a Raspberry Pi. Main features: simple config interface, stability, and won't mess up your video streaming or bittorrent.

THIS IS VERY PRE-ALPHA AT THE MOMENT.

Currently this repo only contains Pi-specific binary .deb packages of the latest Tor releases (experimental) that will work on a Raspberry Pi.  *If you don't trust binary packages from a random dude on Github,* you can find instructions to build them from source yourself - this will take 30-40 minutes on a Pi.  Please see https://www.torproject.org/docs/debian.html.en#source

All but the packages older than 0.2.4.15-rc have been signed with my public key, 0x1EEFFBA3.  Never versions of this document will contain instructions on how to validate that the .debs provided here are provided by me and not tampered with; for now I'll assume you know how to do it.
