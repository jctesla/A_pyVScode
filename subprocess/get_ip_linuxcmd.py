import subprocess
ip = subprocess.check_output(["hostname","-I"])
print(f"La Ip de tu raspBerry es = {ip}\n")

# lo prove en RaspBerry pi 4
# pi@raspi:~ $ python3 run_linux_cmd.py
# La Ip de tu raspBerry es = b'192.168.1.66 2001:1388:111:705f:ca80:32e5:fd7d:d5a2 \n'
