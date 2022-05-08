#to check the special number or not

def main():
    num = int(input('enter the number:'))
    sum = 0
    product = 1
    temp = num

    while num>0:
        digit = num%10
        sum = sum + digit
        product = product * digit
        num = num//10

    if (product + sum)==temp:
        print(f'{temp} is a special number')

    else:
        print(f'{temp} is not a special number')
main()
