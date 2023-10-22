def solution(number):
    if number <3:
        return 0
    sum=0
    for i in range(3,number):
        if i%3==0 or i%5==0:
            sum = sum+i
    return sum