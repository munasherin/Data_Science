pairs_list = []

print("Enter key-value pairs (Type 'done' when you are finished):")

try:
    while True:
        user_input = input("Enter pair (Format: key:value): ").strip()

        if user_input.lower() == 'done':
            break

        if ":" in user_input:
            # Split at the first colon only, then clean up extra spaces
            key, value = user_input.split(sep=":", maxsplit=1)
            key, value = key.strip(), value.strip()

            if not key:
                print("⚠ Key cannot be empty. Please use 'key:value' (e.g., age:21)")
                continue

            if not value:
                print("⚠ Value cannot be empty. Please use 'key:value' (e.g., age:21)")
                continue

            if any(k == key for k, _ in pairs_list):
                print(f"ℹ Key '{key}' already exists; the latest value will be used.")

            pairs_list.append((key, value))
        else:
            print("⚠ Invalid format. Please use 'key:value' (e.g., age:21)")

except (EOFError, KeyboardInterrupt):
    print("\nInput interrupted. Showing what was entered so far.")

# Convert the list of pairs into a tuple
nested_tuple = tuple(pairs_list)
print(f"\nGenerated Tuple: {nested_tuple}")

# Convert tuple to dictionary
result_dict = dict(nested_tuple)
print(f"Resulting Dictionary: {result_dict}")