#to find the number is automorphic or not

def main():
    num= int(input('enter the number:')) 
    square = num * num
    flag = 0

    while(num>0):
        if num%10!=square%10:
            print(f'number is not automorphic')
            flag = 1
            break
        num = num//10
        square = square//10

    if (flag==0):
        print(f'the number is automorphic')

main()

