 
n = int(input("n:"))

def sum_of_n(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_n(num - 1)
print("The sum is:", sum_of_n(n))

