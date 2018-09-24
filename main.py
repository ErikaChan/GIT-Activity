def make_sqaure(size):
    li = []
    for i in range(0, size):
        li.append('*')
    s = "".join(li)
    for i in range(0, size):
        print(s)

def make_rectangle(length, width):
    pass

def make_triangle(size):
    pass

def main():
    while(True):
        print('Hello, please enter what to print')
        print('1\tsquare')
        print('2\trectangle')
        print('3\ttriangle')
        shape = (int)(input('Input: '))
        if(shape == 1):
            size = (int)(input('Input size:'))
            make_sqaure(size)
        elif(shape == 2):
            length = (int)(input('Input length: '))
            width = (int)(input('Input width: '))
            make_rectangle(length, width)
        elif(shape == 3):
            size = (int)(input('Input size: '))
            make_triangle(size)

main()
