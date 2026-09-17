services = ["database", "backend", "frontend"]

print("Deployment order:")

for position, service in enumerate(services, start=1):
    print(f"{position}. Deploy {service}")

print("Deployment sequence prepared.")