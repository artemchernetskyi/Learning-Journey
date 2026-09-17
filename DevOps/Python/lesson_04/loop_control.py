services = ["web-api", "database", "cache"]

print("Starting service scan...")

for service in services:
    print(f"Checking {service}")

    if service == "database":
        print("Critical database issue found.")
        break

    print(f"{service}: check passed")

print("Service scan ended.")

print("\nStarting deployment loop...")

for service in services:
    if service == "database":
        print("Skipping database deployment.")
        continue

    print(f"Deploying {service}")

print("Deployment loop ended.")