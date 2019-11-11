import random

letter = ord('a')
alphabet = [chr(i) for i in range(letter, letter+26)]
key = alphabet.copy()
random.shuffle(key) 

def cipher(plain_text, key):
    text_list = list(plain_text)
    temp = []
    for x in text_list: 
        if x in alphabet:
            temp.append(key[alphabet.index(x)])
    return ''.join(temp)

def decipher(cipher_text, key):
    text_list = list(cipher_text)
    temp = []
    for x in text_list:
        if x in key:
            temp.append(alphabet[key.index(x)])
    return ''.join(temp)

def main():
    while(True):
        text = input("Enter the text: ")
        option = int(input("Choose the option: \n1) Encrypt\n2) Decrypt\n=>"))
        if option==1:
            print("The encrypted text of {} is \n{}".format(text, cipher(text, key)))
        elif option==2:
            print("The decrypted text of {} is \n{}".format(text, decipher(text, key)))

        to_break = input('Do you want to continue (Y/n)? ')
        if to_break.lower()=='n' or to_break.lower()=='no':
            exit()

if __name__=="__main__":
    main()