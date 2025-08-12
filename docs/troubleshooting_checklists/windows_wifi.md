# Windows Wi-Fi Troubleshooting - Quick Checklist

1. Confirm Airplane mode is off and Wi-Fi is on.
2. Check physical switch or hotkey if applicable.
3. Forget and reconnect to the SSID.
4. `ipconfig /all` - confirm adapter has IPv4 and DNS.
5. `ipconfig /flushdns` then try `nslookup example.com`.
6. Test `ping 8.8.8.8` then `ping example.com` to compare DNS vs connectivity.
7. Disable then enable adapter in Network Connections.
8. Temporarily disable VPN, proxy, or third party firewall.
9. Update driver from OEM site.
10. If multiple devices are impacted, reboot modem/router and check ISP status.