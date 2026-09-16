server_fleet = [
    {
        "name": "web-01",
        "role": "web",
        "active": True,
    },
    {
        "name": "db-01",
        "role": "database",
        "active": False,
    },
]

print(server_fleet)
print(type(server_fleet))
print(type(server_fleet[0]))

primary_server_name = server_fleet[0]["name"]
database_server = server_fleet[1]
database_ready = database_server["active"]

print(f"Primary server: {primary_server_name}")
print(f"Database server: {database_server['name']}")
print(f"Database ready: {database_ready}")

if database_ready:
    print("Database status: READY")
else:
    print("Database status: WARNING")