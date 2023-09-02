# fail2ban_tool

Because the home IP does not change easily, and port-forwarded servers are constantly spoofed.
Until I bought a designated firewall, I wanted to generate an easy-to-use tool based on "Fail2ban" package.

-This is an easy Python script that shows fail2ban log results in real-time in a user-friendly way (extracted from fail2ban.log).

-The former version fail2ban.py, lists the possible threads clustered under Yesterday, Today, and Now (the second you turned on the tool).

-Later versions of the tool (fail2ban_10, fail2ban_10_now) can ban the thread according to the location after a WHOIS search.

-As can be understood from the naming, fail2ban_10 shows Yesterday, Today, & Now and is capable of banning the thread. fail2ban_10_now only shows Now and as capable of doing the WHOIS and banning according to the location.


Cheers!
