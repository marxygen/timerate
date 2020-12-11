import sys
sys.path.append(r'C:\\Users\\Asus\\timerate\\') 

from timerate.static import timed, avgtime

@timed
def example1(N):
    a, b = 0, 1
    fibs = []
    for x in range(N):
        fibs.append(a)
        a, b = b, a+b

    return fibs

@avgtime(100)
def example2(N):
    [x for x in range(N)]

if __name__ == '__main__':
    print(example1(5))
    print(example2(1000))