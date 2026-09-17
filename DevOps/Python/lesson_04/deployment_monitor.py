services = [
    {
        "name": "web-api",
        "status": "running",
        "replicas": 3,
        "required_replicas": 3,
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

ready_count = 0
warning_count = 0
critical_count = 0
skipped_count = 0
problem_services = []

for position, service in enumerate(services, start=1):
    if service["status"] == "maintenance":
        print(f"{position}. {service['name']}: SKIPPED (maintenance)")
        skipped_count += 1
        continue
    elif service["status"] == "stopped" or service["replicas"] == 0:
        print(f"{position}. {service['name']}: CRITICAL")
        problem_services.append(service["name"])
        critical_count += 1
    elif service["replicas"] < service["required_replicas"]:
        print(f"{position}. {service['name']}: WARNING")
        problem_services.append(service["name"])
        warning_count += 1
    else:
        print(f"{position}. {service['name']}: READY")
        ready_count += 1

print(f"Problem services: {problem_services}")
print(f"Ready services: {ready_count}")
print(f"Warning services: {warning_count}")
print(f"Critical services: {critical_count}")
print(f"Skipped services: {skipped_count}")
