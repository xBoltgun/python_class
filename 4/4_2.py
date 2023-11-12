from itertools import product
key_dict = {
        "1" : ["1", "2", "4"],
        "2" : ["1", "2", "3", "5"],
        "3" : ["2", "3", "6"],
        "4" : ["1", "4", "5", "7"],
        "5" : ["2", "4", "5", "6", "8"],
        "6" : ["3", "5", "6", "9"],
        "7" : ["4", "7", "8"],
        "8" : ["5", "7", "8", "9", "0"],
        "9" : ["6", "8", "9"],
        "0" : ["8", "0"]
    }
def get_pins(observed): 

    # 根据输入得到二维数组
    nested_list =[  key_dict[ch]  for ch in observed ]
# 最后将所有组合的数字列表转化为字符串
    return ([''.join(item) for item in product(*nested_list)])