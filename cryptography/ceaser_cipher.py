def encrypt(plain_text, key):
  temp = []
  text_list = list(plain_text)

  for x in text_list:
    if x.islower():
      temp.append(chr((ord(x) + key -97) % 26 +97))
    elif x is ' ':
        temp.append(' ')
    else:
      temp.append(chr((ord(x) + key - 65) % 26 +65))
  return ''.join(temp)

def decrypt(cipher_text, key):
  temp = []
  text_list = list(cipher_text)

  for x in text_list:
    if x.islower():
      temp.append(chr((ord(x) - key -97) % 26 +97))
    elif x is ' ':
        temp.append(' ')
    else:
      temp.append(chr((ord(x) - key - 65) % 26 +65))
  return ''.join(temp)

key = int(input("Enter the key: "))
choice = input("Choose one of the option: \n1)Encrypt\n2)Decrypt\n->")
if choice is '1':
    plain_text = input("Enter the text: ")
    cipher_text = (encrypt(plain_text, key))
    print(f'The encrypted of given input: "{plain_text}" is\n"{cipher_text}"')
elif choice is '2':
    cipher_text =  input("Enter the Cipher text: ")
    plain_text = decrypt(cipher_text, key)
    print(f'The encrypted of given input: "{cipher_text}" is\n"{plain_text}"')
else:
    print("Invalid Input!")
