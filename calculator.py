                        ###两个数的简单计算器###
###INSTRUCTION:
###编写一个简单计算器程序，可根据输入的运算符，
###对2个数进行加、减、乘、除或求余运算。

###输入格式：
###输入在一行中依次输入操作数1、运算符、操作数2，其间以1个空格分隔。
###操作数的数据类型为整型或浮点型，且保证除法和求余的分母非零。
###输出格式：
###当运算符为+、-、*、/、%时，在一行输出相应的运算结果。
###若输入是非法符号（即除了加、减、乘、除和求余五种运算符以外的其他符号）则输出ERROR。

def calculator(n):
    '''Function as a calculator

    Examples:
    >>> calculator('-7 / 2')
    -3.5

    >>> calculator('3 & 6')
    ERROR
    '''
    import re

    num = re.findall('\D?\d+\.?\d*', n) #提取数字
    num = [float(x) for x in num]
    operator = re.findall('\s\D+\s', n)[0].strip() # 提取符号

    run_dict = {'+': num[0]+num[1],
                '-': num[0]-num[1],
                '*': num[0]*num[1],
                '/': num[0]/num[1],
                '%': num[0]%num[1]}
    if not run_dict.get(operator):
        print("ERROR")
        return
    print(run_dict.get(operator))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Test has passed.\n")
    calculator(input('Do your calculation:\n> '))
