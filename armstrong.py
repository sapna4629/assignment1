#to check the num is armstrong or not

def main():
    num = int(input('enter the n number:'))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(f'{num} is an armstrog number')

    else:
        print(f'{num} is not an armstrong number')

main()