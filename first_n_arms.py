#first n armstrong number
def main():
    num= int(input('enter the number:'))
    first_n_arm(num)

def first_n_arm(num):
    for var in range(1, num+1):
        i = len(str(var))
        sum = 0
        temp = var

        while temp>0:
            digit = temp%10
            sum = sum + digit**i
            temp //= 10

        if var == sum:
            print(var)        

main()
