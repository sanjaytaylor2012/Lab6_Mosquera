def encode(password):
    encoded = ""
    for i in range(len(password)):
        current = int(password[i])
        current += 3
        if current > 9:
            current %= 10
        encoded += str(current)
    return encoded


encoded_pass = ""
while True:
    print("""
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

    # elif option == "2":
            # decoded_pass = decode(encoded_pass)
            # print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}')
    elif option == "3":
        quit()



