import Day_11_Capstone.art as art 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  'a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(start_text,shift_amount,cipher_direction):
  end_text = ""
  if cipher_direction == 'decode':
      shift_amount *= -1 
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here is the {cipher_direction}d result: {end_text}")



statement = True
while statement:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text= text,shift_amount=shift,cipher_direction=direction)
  decision = input(f"Type 'yes' if you want to go again. Else type 'no' to quit.\n")
  if decision == 'no':
    statement = False
    print("Goodbye")

"""#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    string_encrypt = alphabet[new_position]
    cipher_text += string_encrypt
  print(f"The encoded text is {cipher_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def decrypt(d_plain_text,d_shift_amount):
  cipher_text = ""
  alpha_full = 26
  for letter in d_plain_text:
    position = alphabet.index(letter)
    full_position = position + alpha_full
    new_position = full_position - d_shift_amount
    string_encrypt = alphabet[new_position]
    cipher_text += string_encrypt
  print(f"The decoded text is {cipher_text}")


if direction == 'encode':
  encrypt(plain_text = text, shift_amount = shift)
elif direction == 'decode':
  decrypt(d_plain_text = text, d_shift_amount = shift)
else:
  print("try again")
"""


"""
  if direction == 'encode':
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      string_encrypt = alphabet[new_position]
      cipher_text += string_encrypt
    print(f"The encoded text is {cipher_text}")
  elif direction == 'decode':
    cipher_text = ""
    alpha_full = 26
    for letter in plain_text:
      position = alphabet.index(letter)
      full_position = position + alpha_full
      new_position = full_position - shift_amount
      string_encrypt = alphabet[new_position]
      cipher_text += string_encrypt
    print(f"The decoded text is {cipher_text}")
  else:
    print("Try again: Re-run the program")


caesar(plain_text= text,shift_amount=shift)
"""

  