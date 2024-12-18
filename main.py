def binary_to_decimal(binary):
    decimal = 0
    binary_str = str(binary)  # Convert binary number to string
    length = len(binary_str)

    for i in range(length):
        bit = int(binary_str[i])  # Extract each digit
        decimal += bit * (2 ** (length - i - 1))  # Multiply by 2^(position)
    
    return decimal

# Input: Binary number as an integer
binary_number = int(input("Enter a binary number: "))
decimal_number = binary_to_decimal(binary_number)

print(f"The decimal equivalent of binary {binary_number} is {decimal_number}.")
