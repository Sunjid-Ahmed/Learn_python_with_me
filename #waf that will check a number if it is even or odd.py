#waf that will check a number if it is even or odd
num=int(input("num:"))

def check_num(number):
    if number%2==0:
        print("even")
    else:
        print("odd")
check_num(num)            