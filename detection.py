import psutil

suspicious_ports = [4444, 1234, 9999, 5555]

for conn in psutil.net_connections():
    if conn.lport in suspicious_ports or conn.rport in suspicious_ports:
        print(f"[ALERT] Suspicious port detected: {conn.lport} -> {conn.rport}")

print("Scan complete")
