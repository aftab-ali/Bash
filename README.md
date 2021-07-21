## Bash
To perform a nmap scan over the found IPs in your network. 
&nbsp
for ip in $(cat filename.txt); do nmap -O $ip;
