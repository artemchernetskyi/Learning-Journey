services = [
    {"name": "web-api", "status": "READY"},
    {"name": "worker", "status": "WARNING"},
    {"name": "database", "status": "CRITICAL"},
]
def describe_service(name, status="UNKNOWN"):
    """Return a readable health description for a service."""
    if status == "READY":
        return f"{name}: healthy"
    if status == "CRITICAL" or status == "WARNING":
        return f"{name}: problem ({status})"

    return f"{name}: unknown status"

for service in services:
    message = describe_service(service["name"], service["status"])
    print(message)

print(describe_service("scheduler"))