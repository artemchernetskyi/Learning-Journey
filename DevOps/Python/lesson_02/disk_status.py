disk_usage = int(input("Enter disk usage percentage: "))
cpu_usage = int(input("Enter CPU usage percentage: "))
both_resources_normal = disk_usage < 80 and cpu_usage < 80
print(f"Both resources normal: {both_resources_normal}")
maintenance_mode = False
alerts_enabled = not maintenance_mode

print(f"Alerts enabled: {alerts_enabled}")

if disk_usage >= 90 or cpu_usage >= 90:
    print("CRITICAL: Resource usage is very high.")
elif disk_usage >= 80 or cpu_usage >= 80:
    print("WARNING: Resource usage is high.")
else:
    print("OK: Resource usage is normal.")
