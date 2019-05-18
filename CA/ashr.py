# Program for Arithmetic Shift Right

def ashr(number):
    k=[]
    k.append(number[0])
    for x in range(0,len(number)-1):
        k.append(number[x])
    ans = ''.join(k)
    return ans

if __name__ == '__main__':

    b = '10001'
    b_list = b.split()
    print(f'The actual number: {b}')
    print(ashr(b))
