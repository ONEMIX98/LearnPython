                            ###超速判断###
###INSTRUCTION:
###模拟交通警察的雷达测速仪。
###输入汽车速度，如果速度超出60 mph，则显示“Speeding”，否则显示“OK”。

###输入格式：
###输入在一行中给出1个不超过500的非负整数，即雷达测到的车速。
###输出格式：
###在一行中输出测速仪显示结果，格式为：Speed: V - S，其中V是车速，S或者是Speeding、或者是OK。
def detect(vel):
    '''
    Function to detect if speeding.

    Examples:

    >>> detect(40)
    Speed: 40 - OK
    >>> detect(75)
    Speed: 75 - Speeding
    >>> detect(600)
    Traceback (most recent call last):
        ...
    ValueError: Expected velocity range: 0 - 500

    '''
    limit = 60
    if 0<= int(vel) <= 500:
        print(f'Speed: {vel} - OK') if int(vel)<=60 else print(f'Speed: {vel} - Speeding')
    else:
        raise ValueError('Expected velocity range: 0 - 500')
if __name__ == '__main__': #若作为文件直接执行
    import doctest
    doctest.testmod()
    print("Test has passed.\n")
    detect(input('Your speed:\n> '))
