#wap to check if a list contains a palindrome of elements(copy() method)
list=[1,"abc","abc",1]
list1=list.copy()
list1.reverse()
if list1==list:
    print("it is a palindrome")
else:
    print("it is not a palindrome")