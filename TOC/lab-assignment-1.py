#!/usr/local/bin/python3

def set_char(char_def):
    numberOfChar = int(input("Enter the number of set characters: "))
    for i in range(0, numberOfChar):
        char_def.append(input("Set the {} character to: ".format(i+1)))

def v1():
    index = 0
    char_def = []
    set_char(char_def)
    characters = input("Enter the characters followed by space: ")
    input_char_list = characters.split()

    for input_char in input_char_list:
        while(True):
            if not(char_def[0]==input_char or char_def[1]==input_char):
                print("The input doesn't match. Please try again!")
                input_char = input("Enter the character: ")
                input_char_list[index] = input_char
            else:
                break
        index = index + 1
    print("The final string is: {}".format(''.join(input_char_list)))

def v2():
    char_def = []
    input_char =[]
    set_char(char_def)
    itr = int(input("Enter the number of characters: "))
    
    for i in range(0, itr):
        while True:
            temp = input("Enter the {} character: ".format(i+1))
            if not(temp in char_def):
                print("The character doesn't match. Try Again!") 
            else:
                input_char.append(temp)
                break
    print("The final string is: {}".format(''.join(input_char)))

if __name__ =="__main__":
    option = int(input("Choose (1) v1.0 or (2) v2.0: "))
    if option is 1:
        v1()
    elif option is 2:
        v2()
    else:
        print("Invalid Choice")
