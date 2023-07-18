#Diamond Nicholas COP3502C
#Lab 6 - Group 3: Version Control 

def encoder(password):
  new_password = ''
  
  for num in password:
    number = int(num) + 3
    #when an ecoded number reaches 10, its suppose to reset to zero and continue counting up.
    if number >= 10:
      number = str(number)[1] #changes 10--> 0, 11--> 1, 12--> 2 by only taking the 2nd digit
    new_password += str(number)

  return new_password


def decoder(password):
  pass


def main():
  quit_program = False

  while quit_program == False:
    #Menu and its options here.
    print('Menu\n-------------')
    print('1. Encode\n2. Decode\n3. Quit\n')
    option = int(input('Please enter an option: '))
  
    if option == 1:
      #encode password option here
      password = str(input('Please enter your password to encode: '))
      print('Your password has been encoded and stored!\n')
      encode_password = encoder(password)
  
    elif option == 2:
      #decode password option here
      decode_password = decoder(encode_password)
      print(f'The encoded password is {encode_password}, and the original password is {decode_password}.\n')

    elif option == 3:
      #quit option here
      quit_program = True

    else:
      #error message when option 1-3 isnt selected.
      print('Invalid. Please select again.\n')


if __name__ == '__main__':
  main()