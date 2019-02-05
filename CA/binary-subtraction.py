# Program to subtract two binary numbers using 2's complement method.

def compliment(x):
    array = list(x)
    for i in range(0,len(array)):
        if(array[i]=='0'):
            array[i]='1'
        else:
            array[i]='0'
    x=''.join(array)
    return x

def binary_addition(x,y):
    firstNumber = list(x)
    secondNumber = list(y)
    result=[]
    c=0
    counter=len(firstNumber)-1
    for i in range(0,len(firstNumber)):
        temp = int(firstNumber[counter]) + int(secondNumber[counter]) + c
        if(temp>1):
            c=1
            temp=temp%2
        else:
            c=0
        result.append(str(temp))
        counter = counter - 1

    out=''.join(result)
    return out[::-1]

def binary_subtraction(x,y):
    y=compliment(y)
    y=increment(y)
    return binary_addition(x,y)

def increment(a):
    result=binary_addition(a,'0'*(len(a)-1)+'1')
    return result

def main():
    a=input("Enter frist number: ")
    b=input("Enter second number: ")
    print(binary_subtraction(a,b))

if __name__ == '__main__':
    main()