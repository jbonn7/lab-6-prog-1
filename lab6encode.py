#Justin Bonn's first github addition

def encode(pw):
    encoded_pw = ''
    for i in range(len(pw)):
        encoded_pw += str(((int(pw[i]) - 3) % 10))

    return encoded_pw



def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

        user_option = input('Please enter an option: ')

        if user_option == '1':
            password = input('Please enter your password to encode: ')
            encode(password)

        elif user_option == '2':
            pass #placeholder for decode function

        else:
            break

if __name__ == '__main__':
    main()
