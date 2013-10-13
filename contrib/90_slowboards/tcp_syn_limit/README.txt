This is for slow boards - the specific settings here are tuned for my Raspberry
Pi, which is overclocked to 950MHz and runs entirely on a Class 10 microSDHC
card.

1. Add the iptables lines to the end (above the 'exit 0' line) of /etc/rc.local
   and ADJUST THE PORTS to match your ORPort and DirPort.
 
   Note that I found through trial and error that limiting TCP SYNs on those
   ports to 4 per second with a burst limit of 10 is a very good balance, on
   a 950MHz Raspberry Pi, to balance between relaying traffic and defending
   against "circuit creation storms," or any other uncommon SYN flood of your
   ORPort (more common) or DirPort (never seen it).  If you are running a
   faster or slower machine, you may want to tune this - especially if you
   plan to relay more than about 2Mbps.

2. Install fail2ban ('aptitude install fail2ban') and then put the files in
   fail2ban/ in /etc/fail2ban/

This is PRE-alpha and HAS NOT been battle-tested yet.  I wrote it during a
circuit creation / SYN storm but the storm abated before I'd figured out the
proper fail2ban jail syntax.
