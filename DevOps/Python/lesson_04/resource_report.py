servers = [
    {"name": "web-01", "cpu_usage": 45},
    {"name": "db-01", "cpu_usage": 92},
    {"name": "cache-01", "cpu_usage": 75},
]

ok_count = 0
warning_count = 0
critical_count = 0

print("CPU usage report:")

for server in servers:
    name = server["name"]
    cpu_usage = server["cpu_usage"]

    if cpu_usage >= 90:
        status = "CRITICAL"
        critical_count += 1
    elif cpu_usage >= 70:
        status = "WARNING"
        warning_count += 1
    else:
        status = "OK"
        ok_count += 1

    print(f"{name}: CPU {cpu_usage}% - {status}")

print(f"OK: {ok_count}")
print(f"WARNING: {warning_count}")
print(f"CRITICAL: {critical_count}")