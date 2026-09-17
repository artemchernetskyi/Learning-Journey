attempt = 1
max_attempts = 3

print("Starting while retry loop...")

while attempt <= max_attempts:
    print(f"Attempt {attempt} of {max_attempts}")
    attempt += 1

print(f"Final attempt value: {attempt}")
print("Retry loop completed.")