# to print the first n prime numbers 

def main():
    num = int(input('enter the number:'))
    start = 1

    for num in range(start, num+1):
        if (num>1):
            for i in range(2, num):
                if (num%i)==0:
                    break
            else:
                print(num)
main()
            
