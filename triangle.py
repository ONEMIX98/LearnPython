                                ###输出三角形###
###INSTRUCTION: 编写程序，输出指定的由“*”组成的三角图案。

###输入格式：
###整数n，表示三角形的行数
###输出格式：
###按照下列格式输出由“*”组成的三角图案。

def triangle(n):
    '''
    Function to draw triangle.

    Examples:

    >>> triangle(4)
    ****
    ***
    **
    *
    '''
    n = int(n)
    if n == 0:
        return
    print('*' * n)
    return triangle(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Test has passed.\n")
    triangle(input('Number of rows:\n> '))
