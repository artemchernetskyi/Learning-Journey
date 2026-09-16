deployment_targets = ["dev-01", "staging-01", "prod-01"]

print(deployment_targets)

deployment_targets[0] = "dev-02"
deployment_targets.append("backup-01")

server_to_remove = "staging-01"
if server_to_remove in deployment_targets:
    deployment_targets.remove(server_to_remove)
    print(f"Removed server: {server_to_remove}")

production_available = "prod-01" in deployment_targets
print(f"Is prod-01 available: {production_available}")

first_target = deployment_targets[0]
last_target = deployment_targets[-1]
priority_targets = deployment_targets[0:2]

print(f"First target: {first_target}")
print(f"Last target: {last_target}")
print(f"Priority targets: {priority_targets}")

print(f"Total targets: {len(deployment_targets)}")