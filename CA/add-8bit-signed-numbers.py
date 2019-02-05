'''
Program to add two 8-bit SIGNED numbers by using 2’s complement method
''' 
def check_8bit(x , y):
    if (len(x) and len(y))!=8:
        return True
    return False

def signed_twos_complement(x, y):
    counter = len(x)-1
    sum1 = []
    carry=0
    for i in range(0, 8):
        temp_sum = int(x[counter]) + int(y[counter]) + carry
        if (temp_sum>1):
            carry = 1
            temp_sum=temp_sum%2
        else:
            carry=0
        
        sum1.append(str(temp_sum))
        counter=counter-1
            
    if(carry==1):
        sum1.append('1')

    result=''.join(sum1)
    #print('The sum of %s and %s is: ')
    print(result[::-1])
    
if __name__=='__main__':
    first_input = input("Enter the first 8 bit binary number: ")
    second_input = input("Enter the second 8 bit binary number: ")
    x = list(first_input)
    y = list(second_input)
    if check_8bit(x,y):
        print("First or Second number is greater than 8-bit!")
    else:
       signed_twos_complement(x,y)
       input('Press any key!')
