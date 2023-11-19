def shorten_number(suffixes, base):
    def my_filter(data):
        try:
            # 将函数输入转换为整数
            number = int(data)
            
        # 如果输入的数据不能转换为整数，直接转换为str返回
        except (TypeError, ValueError):
            return str(data)
        
        # 输入的number可以转换为整数
        else:
            # i用来跟踪suffixes列表的索引
            i = 0
            
            # 每次循环将输入的数字除以base，索引i+1
            # 如果除以base等于0或者索引等于len(suffixes)-1，结束循环
            while number//base > 0 and i < len(suffixes)-1:
                number //= base
                i += 1
            return str(number) + suffixes[i]     

    # 返回值是一个函数
    return my_filter
