add = lambda a,b,c: a+b+c    
a,b,c = 1,2,3

def curry_partial(f, *args):  
    
    # 如果f不是函数，直接返回
    if not callable(f): 
        return f

    # 查看函数f需要的参数个数
    num_args = f.__code__.co_argcount

    # 如果f函数不需要参数，说明f是curry_partial函数
    if num_args == 0:
        return f(*args)

    if len(args) >= num_args:
        return f(*args[:num_args])

    def inner(*params):    
        all_args = [*args, *params]

        # 如果没有参数，这是curry函数，使用链式调用
        if not args:
            return curry_partial(f, *all_args)

        # 如果第一个参数不是函数，这是curry函数，使用链式调用        
        if not callable(args[0]):
            return curry_partial(f, *all_args)

        # 如果第一个参数是函数，这是partial函数，使用部分函数调用
        fn = args[0]
        num_args2 = fn.__code__.co_argcount

        # 如果fn函数不需要参数，说明fn是curry_partial函数
        if num_args2 == 0:
            return fn(*all_args)

        if len(all_args) >= num_args2:
            return fn(*all_args[:num_args2])
        else:
            return curry_partial(fn, *all_args)
        
    return inner

# 定义一个三个数的加法
add = lambda a,b,c: a+b+c    
a,b,c = 1,2,3

# partial调用
print(curry_partial(curry_partial(curry_partial(add, a), b), c))

# curry调用
print(curry_partial(add)(a)(b)(c))