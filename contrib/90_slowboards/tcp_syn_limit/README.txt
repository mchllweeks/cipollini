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
   the appropriate fail2ban directory here in /etc/fail2ban/.

   Debian wheezy ships with fail2ban 0.8.6, which does not yet support
   jail.d, so use the 'older' directory.  If you have fail2ban 0.8.11 or
   newer, you can use the 0.8.11 directory.

   Note that on startup, on a slow machine, fail2ban-server MAY chew up a
   lot of CPU time for a minute or five, especially if you've installed it
   with a lot of noise already in the logs - it has to parse the most recent
   log files from top to bottom before it settles in; this is normal.

This is PRE-alpha and HAS NOT been battle-tested yet.  I wrote it during a
circuit creation / SYN storm but the storm abated before I'd figured out the
proper fail2ban jail syntax.

Immediate tinkering suggestion: reduce findtime to 60, bantime to 90, to maybe
preserve already-connected peers who had circuits through us, or at least not
choke them off so bad, even if they close their circuits within 90 seconds of
silent treatment.
