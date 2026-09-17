servers = ["web-01", "db-01", "cache-01"]

print("Starting server checks...")

ok_count = 0
warning_count = 0

for server in servers:
    if server == "db-01":
        print(f"{server}: WARNING")
        warning_count += 1
    else:
        print(f"{server}: OK")
        ok_count += 1

print(f"OK servers: {ok_count}")
print(f"Warning servers: {warning_count}")
print("All checks completed.")
