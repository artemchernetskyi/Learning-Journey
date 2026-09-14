server_name = input("Enter the server name: ")
running_containers_text = input("Enter the number of running containers: ")

running_containers = int(running_containers_text)
monitoring_enabled = True
containers_after_deployment = running_containers + 1

print(f"Server: {server_name}")
print(f"Running containers: {running_containers}")
print(f"Monitoring enabled: {monitoring_enabled}")
print(f"Containers after deployment: {containers_after_deployment}")

print()

disk_usage_text = input("Enter disk usage percentage: ")
disk_usage = int(disk_usage_text)
warning_threshold = 80
disk_warning = disk_usage >= warning_threshold

print(f"Disk usage: {disk_usage}%")
print(f"Warning threshold: {warning_threshold}%")
print(f"Disk warning: {disk_warning}")