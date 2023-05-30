# Define the string
message = "Hello World"

and_result = ''.join(chr(ord(char) & 127) for char in message)
xor_result = ''.join(chr(ord(char) ^ 127) for char in message)
or_result = ''.join(chr(ord(char) | 127) for char in message)

# Print the results
print("Original message:", message)
print("AND result:", and_result)
print("XOR result:", xor_result)
print("OR result:", or_result)