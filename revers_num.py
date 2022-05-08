#revers a number

def main():
    num = int(input('enter a number:'))
    display_reverse(num)

def display_reverse(num):
    reverse_num=0

    while num != 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    print(int(reverse_num))

main()