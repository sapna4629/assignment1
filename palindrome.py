#to check the number is palindrome or not

def main():
    num= int(input('enter the number:'))
    palindrome(num)

def palindrome(num):
    temp = num
    rev = 0

    while num>0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        print(f'{temp} is palindrome')
        
    else:
        print(f'{temp} is not a palindrome')
main()
