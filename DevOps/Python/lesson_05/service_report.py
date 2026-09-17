services = [
    {
        "name": "web-api",
        "status": "running",
        "replicas": 3,
        "required_replicas": 2,
    },
    {
        "name": "worker",
        "status": "running",
        "replicas": 1,
        "required_replicas": 2,
    },
    {
        "name": "database",
        "status": "stopped",
        "replicas": 0,
        "required_replicas": 1,
    },
]


def service_health(service):
    if service["status"] == "stopped" or service["replicas"] == 0:
        return "CRITICAL"

    if service["replicas"] < service["required_replicas"]:
        return "WARNING"

    return "READY"

problem_services = []
for service in services:
    health = service_health(service)
    print(f"{service['name']}: {health}")
    if health == "CRITICAL" or health == "WARNING":
        problem_services.append(service["name"])
print(f"Problem services: {problem_services}")