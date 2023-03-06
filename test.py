# Najib Mosquera
# Sanjay Taylor
def encode(password):
    encoded = ""
    for i in range(len(password)):
        current = int(password[i])
        current += 3
        if current > 9:
            current %= 10
        encoded += str(current)
    return encoded

# The decode function was added
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        dec_digit = str((int(digit) - 3) % 10)
        decoded_password += dec_digit
    return decoded_password


encoded_pass = ""
decoded_pass = ""
while True:
    print("""S
Menu  
------------- 
1. Encode  
2. Decode  
3. Quit 
    """)

    option = input("Please enter an option: ")


    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_pass = encode(password)
        print("Your password has been encoded and stored!\n")
    elif option == "2":
        decoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}\n')
    elif option == "3":
        quit()



