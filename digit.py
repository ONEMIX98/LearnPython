                            ###Digits output###
###INSTRUCTION:
###本题要求编写程序，分解任意正整数

### 输入格式：
###一个正整数n
###输出格式：
###按照以下格式输出：
###n = 个位数字 + 十位数字*10 + 百位数字*100 +...
###（注意字符之间有空格）
import pdb
def digit(n):
    '''
    Function to break up an integer

    Examples:
    >>> digit('152')
    152 = 2 + 5*10 + 1*100

    >>> digit('1698')
    1698 = 8 + 9*10 + 6*100 + 1*1000
    '''
    # Initialize some useful value
    weight = 1
    result = ''
    for d in n[::-1]: #倒序
        temp = f'+ {d}*{str(weight)} ' if weight > 1 else f'{d} '
        result = result + temp
        weight *=10
    result = result.rstrip() #去掉末尾空格
    print(f"{n} = {result}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Test has passed.\n")
    digit(input('Your integer:\n> '))
