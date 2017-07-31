def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b) #a除最大园盘以外的盘经过c柱移动到b柱
        print("a,c,b process")
        move(1,a,b,c) #a底部最大圆盘放到c柱
        print("a,b,c process")
        move(n-1,b,a,c)  #b柱上的圆盘经过a柱移动到c柱
        print("b,a,c process")

move(3,'A','B','C')
