def service_health(status, running_replicas, required_replicas):
    if status == "maintenance":
        return "SKIPPED"

    if status == "stopped" or running_replicas == 0:
        return "CRITICAL"

    if running_replicas < required_replicas:
        return "WARNING"

    return "READY"


web = service_health("running", 3, 2)
worker = service_health("running", 1, 2)
database = service_health("stopped", 0, 1)
cache = service_health("maintenance", 1, 1)

print(f"Web: {web}")
print(f"Worker: {worker}")
print(f"Database: {database}")
print(f"Cache: {cache}")