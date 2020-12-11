import sys
sys.path.append(r'C:\\Users\\Asus\\timerate\\') 

from timerate.static import timed

@timed
def example1(N):
    a, b = 0, 1
    fibs = []
    for x in range(N):
        fibs.append(a)
        a, b = b, a+b

    return fibs

if __name__ == '__main__':
    print(example1(5))