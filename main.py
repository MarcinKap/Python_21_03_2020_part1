# zadanie 1
def print_room(height, width):
    for h in range(height + 1):
        for w in range(width+1):
            if h%height == 0 and w%width == 0:
                print('*', end='')
            elif h%height == 0 and w%width != 0:
                print('.', end='')
            elif h%height != 0 and w%width == 0:
                print('|', end='')
            else:
                print('.', end='')
        print('')

# zadanie 2
def slice(width):
    seq = list(range(width))
    print(seq[2::3])
    print(seq[::-1])
    print(seq[:2:-2])

# zadanie 3
def unique_elements(seq):
    buf = set()
    for i in range(len(seq), 0, -1):
            x = seq[i-1]
            if x in buf:
                seq.pop(i-1)
            if x not in buf:
                buf.add(x)
    print(seq)
    print(buf)
    pass

# zadanie 4
def my_sorter(seq, priority):
    def helper(x):
        if x not in priority:
            return (0, x)
        return (1, x)
    seq.sort(key=helper)
    print(seq)

# zadanie 5
def prime_numbers_1(seq):
    print(list( map(lambda x: x, filter(lambda x: not list(filter(lambda y:x%y == 0, range(2,x))), seq))))

def prime_numbers_2(seq):
    print([x for x in seq  if all(x % y != 0 for y in range(2, x))])

# zadanie 6
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

# zadanie 7

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def printing_func(*args):
        print('zawartosc z dekoratora')
        print(args)
        print(func.__name__)
        return func(*args)


    return printing_func
@my_decorator
def f(*args):
    print('zawartość funkcji f')

# zadanie 8

def call_counter(func):
    def counter(x):
        counter.calls += 1
        print('ilosc zliczen', x)
        return func(x)
    counter.calls = 0
    return counter

@call_counter
def f2(x):
    return x


# zadanie 9
def reading_file():
    try:
        with open('test.txt', 'r', encoding='UTF-8') as fd:
            data = fd.read()
            words = data.split()
            print(len(words))
    except FileNotFoundError as Ex:
        print(Ex)


# def helper():
#     try:
#         # raise Exception('Message')
#         pass
#     except Exception as Ex:
#         print(Ex)
#     else:
#         print('else')
#     finally:
#         print('finally')



def main():

    # zad1 ROOM
    # height = int(input('Give height:'))
    # width =  int(input('Give width:'))
    # print_room(height+1, width+1)

    # zad2 SLICE
    # width =  int(input('Give width:'))
    # slice(width)

    # zad3
    # seq = [1,1,2,3,5,6,5,5,2,2,1,2,7,7]
    # unique_elements(seq)

    # zad4
    seq = [6, 2, 1, 5]
    priority = [1, 2]
    my_sorter(seq, priority)

    # zad5
    # seq = [1,2,3,4,5,23,23,6,7,8,9,10,11,23,13,14,15,16,17,18,19,20,21,22,23,24]
    # prime_numbers_1(seq)
    # prime_numbers_2(seq)

    # zad6
    # fibonacci_range = 10
    # fib = fibonacci()
    # print([fib.__next__() for i in range(fibonacci_range)])

    # zad7
    # f(5,6,8,9)
    # print('nazwa funkcji f ', f.__name__)

    # zad8
    # for i in range(10):
    #   (f2(i))

    # zad9
    # reading_file()



if __name__ == '__main__':
    main()