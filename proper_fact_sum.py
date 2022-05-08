#to find the proper factors

def main():
    num=int(input('enter a number:'))
    display_factor(num)
    
    if num == 0:
        print(f'{num} is perfect factor')

    #else:
        #list=display_factor(num)

def display_factor(num):
    #sum of factors
    i=1
    sum=0

    while i<num:
        if num%i==0:
            sum = sum+i
        i+=1
    print('the sum of factors is',sum)

    start = 1
    total = 0
          
    while start<=num:
        if num%start==0:
            print(start)
            total+=start
        start+=1
    total-=num

    if total==num:
        print(f'{num} is proper factor')
    else:
        print(f'{num} is not a proper factor')


   
main()