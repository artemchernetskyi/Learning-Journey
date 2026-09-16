allowed_environments = ("staging", "production")

required_packages = {"docker", "curl", "git"}
installed_packages = {"docker", "curl", "nginx"}
# Add "git" to test the READY path.

deployment_queue = ["web-api", "worker", "cache"]

service = {
    "name": "web-api",
    "environment": "production",
    "running_replicas": 3,
    "required_replicas": 2,
    "active": True,
}

missing_packages = required_packages - installed_packages
environment_allowed = service["environment"] in allowed_environments
replicas_ready = service["running_replicas"] >= service["required_replicas"]
packages_ready = len(missing_packages) == 0
service_queued = service["name"] in deployment_queue
deployment_ready = (
    environment_allowed
    and replicas_ready
    and packages_ready
    and service_queued
    and service["active"]
)

print(f"Missing packages: {missing_packages}")
print(f"Environment allowed: {environment_allowed}")
print(f"Replicas ready: {replicas_ready}")
print(f"Packages ready: {packages_ready}")
print(f"Service queued: {service_queued}")
print(f"Deployment ready: {deployment_ready}")

if deployment_ready:
    print("Deployment status: READY")
else:
    print("Deployment status: BLOCKED")