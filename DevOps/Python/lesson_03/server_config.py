server = {
    "name": "web-01",
    "ip": "10.0.0.10",
    "port": 8080,
    "active": True,
}

print(server)
print(type(server))

print(f"Server name: {server['name']}")
print(f"Server IP: {server['ip']}")
print(f"Server port: {server['port']}")
print(f"Server active: {server['active']}")
print(f"Configuration fields: {len(server)}")

print("\nUpdating server configuration...")

server["port"] = 9090
server["active"] = False
server["environment"] = "production"

is_production = server["environment"] == "production"

print(server)
print(f"Updated port: {server['port']}")
print(f"Server active: {server['active']}")
print(f"Environment: {server['environment']}")
print(f"Is production: {is_production}")
print(f"Configuration fields: {len(server)}")

region = server.get("region", "not configured")
ip_exists_before = "ip" in server

removed_ip = server.pop("ip")
ip_exists_after = "ip" in server

print(f"Region: {region}")
print(f"IP existed before removal: {ip_exists_before}")
print(f"Removed IP: {removed_ip}")
print(f"IP exists after removal: {ip_exists_after}")
print(f"Configuration fields: {len(server)}")