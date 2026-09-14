cpu_cores = 4
containers_per_core = 3
running_containers = 10

total_capacity = cpu_cores * containers_per_core
free_slots = total_capacity - running_containers
average_per_core = running_containers / cpu_cores
full_groups = running_containers // cpu_cores
remaining_containers = running_containers % cpu_cores

print(f"Total capacity: {total_capacity}")
print(f"Free slots: {free_slots}")
print(f"Average per core: {average_per_core}")
print(f"Full groups: {full_groups}")
print(f"Remaining containers: {remaining_containers}")