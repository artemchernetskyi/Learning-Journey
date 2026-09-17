def replicas_ready(running_replicas, required_replicas):
    return running_replicas >= required_replicas


web_ready = replicas_ready(3, 2)
database_ready = replicas_ready(0, 1)

print(f"Web ready: {web_ready}")
print(f"Database ready: {database_ready}")

if web_ready:
    print("Web deployment can continue.")

if not database_ready:
    print("Database deployment is blocked.")