a = ['apple', 'apple', 'apple', 'orange', 'banana', 'banana']
b = {}

for c in a:
    # Use .get(key, 0) to safely get the current count or 0 if it's the first time
    b[c] = b.get(c, 0) + 1

print("--- Item Frequency Count ---")
print(b)
print("\n")