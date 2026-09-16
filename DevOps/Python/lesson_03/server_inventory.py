servers = ["web-01", "web-02", "db-01"]

print(servers)
print(type(servers))

print(servers[0])
print(servers[1])
print(servers[2])

print("\nUpdating server inventory...")

servers[1] = "web-02-prod"
servers.append("cache-01")

print(servers)
print(f"Total servers: {len(servers)}")

server_to_remove = "db-01"

if server_to_remove in servers:
    servers.remove(server_to_remove)
    print(f"Removed server: {server_to_remove}")

db_server_active = "db-01" in servers

print(servers)
print(f"Is db-01 active: {db_server_active}")
print(f"Total servers: {len(servers)}")

first_server = servers[0]
last_server = servers[-1]
web_servers = servers[0:2]

print(f"First server: {first_server}")
print(f"Last server: {last_server}")
print(f"Web servers: {web_servers}")