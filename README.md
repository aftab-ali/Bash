## Bash
To perform a nmap scan over the found IPs in your network.
for ip in $(cat filename.txt); do nmap -O $ip;
