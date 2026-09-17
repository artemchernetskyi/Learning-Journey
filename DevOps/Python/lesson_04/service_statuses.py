service_statuses = {
    "web-api": "running",
    "database": "stopped",
    "cache": "running",
}

print("Service statuses:")

healthy_count = 0
unhealthy_services = []

for service, status in service_statuses.items():
    if status == "running":
        print(f"{service}: OK")
        healthy_count += 1
    else:
        print(f"{service}: WARNING")
        unhealthy_services.append(service)

print(f"Healthy services: {healthy_count}/{len(service_statuses)}")
print(f"Unhealthy services: {unhealthy_services}")
print("Status report completed.")
