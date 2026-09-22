services = [
    {"name": "web-api", "status": "READY"},
    {"name": "worker", "status": "WARNING"},
    {"name": "database", "status": "CRITICAL"},
    {"name": "cache", "status": "READY"},
    {"name": "backup", "status": "WARNING"},
]
problem_statuses = ("WARNING", "CRITICAL")
ready_services = []
problem_services = []
unique_statuses = set()

for service in services:
   if service ["status"] in problem_statuses:
      problem_services.append(service["name"])
      unique_statuses.add(service["status"])
   elif service ["status"] == "READY" :
      ready_services.append(service["name"])
      unique_statuses.add(service["status"])

print(
    f"Ready services ({len(ready_services)}): "
    f"{', '.join(ready_services)}"
)

print(
    f"Problem services ({len(problem_services)}): "
    f"{', '.join(problem_services)}"
)

print(
    f"Unique statuses ({len(unique_statuses)}): "
    f"{', '.join(sorted(unique_statuses))}"
)