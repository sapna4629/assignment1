#to check the number is neon or not

def main():
    num = int(input('enter the number:'))
    i = num ** 2
    sum = 0

    while i:
        sum = sum + (i%10)
        i= i//10
    if sum==num:
        print(f'{num} is a neon number')

    else:
        print(f'{num} is not a neon number')
main()