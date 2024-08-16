#waf to find the factorial of n(n is the parameter)
n=int(input("n:"))

def cal_fact(num):
    fact=1
    for el in range(1,num+1):
        fact*=el
    print("the factorial is:",fact)
cal_fact(n)
