service_name = input("service_name: ")
running_replicas = int(input("running_replicas: "))
error_rate = int(input("error_rate: "))
maintenance_mode = False
service_healthy = running_replicas >= 3 and error_rate < 10 and not maintenance_mode

print(f"Service: {service_name}")
print(f"Service healthy: {service_healthy}")

if maintenance_mode:
    print("MAINTENANCE.")
elif running_replicas == 0 or error_rate >= 50:
    print(f"CRITICAL: Service {service_name} requires immediate attention.")
elif not service_healthy:
    print(f"WARNING: Service {service_name} is experiencing issues.")
else:
    print(f"OK: Service {service_name} is healthy.")
