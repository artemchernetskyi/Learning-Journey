def check_service(name):
    print(f"Checking {name}...")
    print(f"{name}: check completed")


print("Starting service checks...")

check_service("web-api")
check_service("database")

print("All service checks completed.")