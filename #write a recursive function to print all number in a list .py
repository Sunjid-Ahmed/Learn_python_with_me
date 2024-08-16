#write a recursive function to print all elements in a list.(hint:use list and index as parameter)

def print_list(list, idx=0):
    if idx==len(list):
        return 
    print(list[idx])
    print_list(list,idx+1)

fruit=["mango","banana","apple","litchi"]

print_list(fruit)