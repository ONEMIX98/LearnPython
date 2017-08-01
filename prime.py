#odd_iter 生成一个无穷奇数数列，作为初始数列（2以外的偶数都不是素数）
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#not_divisible 输入参数n， 内部定义一个匿名函数，输入参数x， 判断x是否能被n整除
def not_divisible(n):
    return lambda x: x % n > 0

#生成无穷素数数列
def prime():
    _iter = odd_iter() #初始数列
    yield 2
    while  True:
        n = next(_iter)
        yield n
        _iter = filter(not_divisible(n), _iter) #得到新的数列

def primes_under_n():
    boundary = int(input("> Boundary: "))
    print("The primes under boundary are: ")
    for n in prime():
        if n < boundary:
            print(n, end = ' ')
        else:
            break

def amount_of_primes():
    i = 0
    amount = int(input("> How many primes: "))
    print(f"The {amount} primes are: ")
    for n in prime():
        if i < amount:
            print(n, end = ' ')
            i = i + 1
        else:
            break

while True:
    print("\n1. Print primes under n;\n2. Print n primes;\n3. Quit")
    opt = input("> ")
    if opt == '1':
        primes_under_n()
    elif opt == '2':
        amount_of_primes()
    elif opt == '3':
        break
    else:
        print("Invalid Input!")
    print("\n")
