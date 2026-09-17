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
    {
        "name": "cache",
        "status": "maintenance",
        "replicas": 1,
        "required_replicas": 1,
    },
]
def service_health(service):
    if service["status"] == "maintenance":
        return "SKIPPED"

    if service["status"] == "stopped" or service["replicas"] == 0:
        return "CRITICAL"

    if service["replicas"] < service["required_replicas"]:
        return "WARNING"

    return "READY"

ready_count = 0
warning_count = 0
critical_count = 0
skipped_count = 0
problem_services = []

for position, service in enumerate(services, start=1):
    health = service_health(service)
    print(f"{position}. {service['name']}: {health}")

    if health == "READY":
        ready_count += 1
    elif health == "WARNING":
        warning_count += 1
        problem_services.append(service["name"])
    elif health == "CRITICAL":
        critical_count += 1
        problem_services.append(service["name"])
    elif health == "SKIPPED":
        skipped_count += 1

print(f"Ready services: {ready_count}")
print(f"Warning services: {warning_count}")
print(f"Critical services: {critical_count}")
print(f"Skipped services: {skipped_count}")
print(f"Problem services: {problem_services}")