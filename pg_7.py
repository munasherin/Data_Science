pairs_list = []

print("Enter key-value pairs (Type 'done' when you are finished):")

while True:
    user_input = input("Enter pair (Format: key:value): ")

    if user_input.lower() == 'done':
        break

    if ":" in user_input:
        # Split by the colon and clean up extra spaces
        key, value = user_input.split(sep=":", maxsplit=1)
        pairs_list.append((key.strip(), value.strip()))
    else:
        print("⚠ Invalid format. Please use 'key:value' (e.g., age:21)")

# Convert the list of pairs into a tuple
nested_tuple = tuple(pairs_list)
print(f"\nGenerated Tuple: {nested_tuple}")

# Convert tuple to dictionary
result_dict = dict(nested_tuple)
print(f"Resulting Dictionary: {result_dict}")