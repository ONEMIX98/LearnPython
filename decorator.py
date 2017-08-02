import functools

def log(*args):
    text = args[0] if isinstance(args[0],str) else ''
    def decorator(func):
        @functools.wraps(func) #保持装饰后的函数的函数名不变
        def wrapper(*args, **kw):
            print(f"begin {text} {func.__name__}():")
            result = func(*args, **kw)
            print(f"end {text} {func.__name__}()")
            return result
        return wrapper
    # if对应着new = log('excute')(new), else对应着new = log(new)
    # decorator(func)--> decorator需要一个函数参数
    return decorator if isinstance(args[0],str) else decorator(args[0])

# 相当于 now = log('excute')(now), 先执行log('excute'),返回
# decorator 函数。 再执行decorator(now), 最终返回的是wrapper函数
@log('excute')
def now():
    print("2017-8-2")

now()
print("now.__name__: ", now.__name__)
