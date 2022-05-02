#area of and perimeter of circle
def main():
    radius = read('enter the radius of a circle:')
    display(radius, area(radius), perimeter(radius))

def read(msg):
    return float(input(msg))

def area(radius):
    return (22/7)*radius**2

def perimeter(radius):
    return 2*(22/7)*radius

def display(radius, area, perimeter):
    print(f'the area and the perimeter of circle with radius of {radius} is {area, perimeter}')

main()

