environments = ("development", "staging", "production")

print(environments)
print(type(environments))

print(f"First environment: {environments[0]}")
print(f"Last environment: {environments[-1]}")
print(f"Environment count: {len(environments)}")

production_exists = "production" in environments
print(f"Production exists: {production_exists}")

# This would cause a TypeError because tuples are immutable:
# environments[0] = "dev"