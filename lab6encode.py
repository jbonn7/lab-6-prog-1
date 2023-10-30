#Justin Bonn's first github addition

encoded_password = ''

def encode(pw):
    global encoded_password
    encoded_pw=""
    for i in range(len(pw)):
        encoded_digit = str(((int(pw[i]) + 3) % 10))
        encoded_pw += encoded_digit
    encoded_password = encoded_pw

    return encoded_pw
def decode(pw):
    decoded_password=""
    for i in range(len(pw)):
        decoded_digit=str((int(pw)-3)%10)
        decoded_password += decoded_digit
    return decoded_password



def main():
    global encoded_password
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

        user_option = input('Please enter an option: ')

        if user_option == '1':
            password = input('\nPlease enter your 8-digit password to encode: ')
            encode(password)
            print(f"\nEncoded password:{encoded_password}")

        elif user_option == '2':
            if encoded_password:
                decoded_password=decode(encoded_password)
                print(f"\nDecoded password:{decoded_password}")


        else:
            break

if __name__ == '__main__':
    main()
