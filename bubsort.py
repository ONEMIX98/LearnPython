                                ###冒泡法排序###
###INSTRUCTION:
###将N个整数按从小到大排序的冒泡排序法是这样工作的：
###从头到尾比较相邻两个元素，如果前面的元素大于其紧随的后面元素，则交换它们。
###通过一遍扫描，则最后一个元素必定是最大的元素。
###然后用同样的方法对前N−1个元素进行第二遍扫描。
###依此类推，最后只需处理两个元素，就完成了对N个数的排序。
###本题要求对任意给定的K（<N），输出扫描完第K遍后的中间结果数列。

###输入格式：
###输入在第1行中给出N和K（1≤K<N≤100），
###在第2行中给出N个待排序的整数，数字间以空格分隔。
###输出格式：
###在一行中输出冒泡排序法扫描完第K遍后的中间结果数列
###，数字间以空格分隔，但末尾不得有多余空格。
#
def bubsort(attr, nums):
    '''
    Function to sort by bubble
    >>> bubsort('6 2', '2 3 5 1 6 4')
    2 1 3 4 5 6

    '''
    N, K = [int(x) for x in attr.replace(' ', '')]
    nums = [int(x) for x in nums.replace(' ','')]
    for k in range(K):
        for n in range(N-1):
            if nums[n] > nums[n+1]:
                nums[n], nums[n+1] = nums[n+1], nums[n]
        N -= 1

        result = ' '.join([f'{x}' for x in nums]).strip()
    print(result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test has passed.\n')
    attr = input('How many numbers and how many turns?\n> ')
    nums = input("Which numbers?\n> ")
    bubsort(attr, nums)
