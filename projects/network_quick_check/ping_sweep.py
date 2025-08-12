import ipaddress, subprocess, sys, csv, platform
from datetime import datetime

def ping(host: str) -> bool:
    win = platform.system().lower() == "windows"
    cmd = ["ping", "-n" if win else "-c", "1",
           "-w" if win else "-W", "200" if win else "1",
           host]
    return subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python ping_sweep.py 192.168.1.0/24")
        sys.exit(1)
    network = ipaddress.ip_network(sys.argv[1], strict=False)
    rows = [["ip", "status"]]
    for ip in network.hosts():
        rows.append([str(ip), "up" if ping(str(ip)) else "down"])
    with open("ping_sweep.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"Wrote ping_sweep.csv ({len(rows)-1} hosts) @ {datetime.now().isoformat(timespec='seconds')}")

if __name__ == "__main__":
    main()
