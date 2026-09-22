services = input("Enter service name:")
cpu_usage = int(input("Enter CPU usage percentage:"))
memory_usage = int(input("Enter Memory usage percentage:"))
both_resources_normal = cpu_usage < 80 and memory_usage <80
print(f"Both resources normal: {both_resources_normal}")
maintenance_mode = False
alerts_enabled = not maintenance_mode
print(f"Alerts enabled: {alerts_enabled}")

average_usage = (cpu_usage + memory_usage) / 2
print(f"Average resource usage for service {services} is: {average_usage:.2f}%")

if not alerts_enabled:
    print("Maintenance mode is enabled. Alerts are disabled.")
elif cpu_usage >= 90 or memory_usage >= 90:
    print(f"CRITICAL: Service {services} Resource usage is very high.")
elif cpu_usage >= 80 or memory_usage >= 80:
    print(f"WARNING: Service {services} Resource usage is high.")
else:
    print(f"Healthy: Service {services} Resource usage is healthy.")
