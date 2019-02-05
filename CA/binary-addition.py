# Program to add two binary numbers using 2's complement method.

'''
    The logic behind the program is the implementation of full adder circuit.
    This program works for the same number of bit(s) for binary addition.
'''

def binary_addition(a,b):
    c=0 #carry bit
    ans =[] #full answer in list
    firstNumber = [int(i) for i in (a)] #spliting the first int argument
    secondNumber = [int(i) for i in (b)] #splitin the second int argument

    #reversing the first and second argument for addition
    firstNumber = firstNumber[::-1]
    secondNumber = secondNumber[::-1]

    for i in range(len(secondNumber)):
        # '^' is an XOR operator in python
        if not (firstNumber[i] and secondNumber[i]) == 1:
            d = firstNumber[i] ^ secondNumber[i] ^ c
            c = 0
        else:
            d = firstNumber[i] ^ secondNumber[i] ^ c
            c = 1
        ans.append(d)
   
    #if the result is more than the number of input(first and second) bit
    if c==1:
        ans.append(c)
    print(ans[::-1])
    
def main():
    firstNumber = str(input("Enter the first number: "))
    secondNumber = str(input("Enter the second number: "))
    binary_addition(firstNumber, secondNumber)

if __name__ == "__main__":
    main()