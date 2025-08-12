import argparse
import platform
import shutil
import subprocess
import sys

DEFAULT_HOSTS = ["8.8.8.8", "1.1.1.1", "google.com"]

def has_ping():
    return shutil.which("ping") is not None

def ping(host):
    # Windows uses -n, Unix uses -c
    count_flag = "-n" if platform.system().lower().startswith("win") else "-c"
    try:
        result = subprocess.run(
            ["ping", count_flag, "2", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=10
        )
        ok = result.returncode == 0
        return ok, result.stdout
    except Exception as e:
        return False, str(e)

def dns_lookup(host):
    # rely on system ping output for reachability and resolution success
    ok, out = ping(host)
    if ok:
        status = "OK"
    else:
        status = "FAIL"
    return status, out

def main():
    parser = argparse.ArgumentParser(description="Quick network triage helper")
    parser.add_argument("--hosts", nargs="*", default=DEFAULT_HOSTS, help="Hosts or IPs to test")
    args = parser.parse_args()

    print("=== Network Quick Check ===")
    print(f"Platform: {platform.platform()}")
    print(f"Python: {platform.python_version()}")
    print(f"Ping available: {'yes' if has_ping() else 'no'}")
    print()

    if not has_ping():
        print("Ping command not found on this system.")
        sys.exit(1)

    for host in args.hosts:
        print(f"--- Testing {host} ---")
        status, output = dns_lookup(host)
        print(f"Status: {status}")
        # Print only first 10 lines to keep it readable
        lines = output.splitlines()
        for line in lines[:10]:
            print(line)
        if len(lines) > 10:
            print("...")
        print()

if __name__ == "__main__":
    main()