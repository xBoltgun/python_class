def fillable(stock, merch, n):
    if merch in stock:
        if stock[merch]>=n:
            return True
    return False