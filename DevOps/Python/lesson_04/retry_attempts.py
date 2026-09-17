max_attempts = 3

print("Starting retry sequence...")

for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt} of {max_attempts}")

print("Retry sequence completed.")

print("\nScheduled retry delays:")

for delay in range(2, 8, 2):
    print(f"Retry after {delay} seconds")