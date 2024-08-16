#waf to print the elements of a list in a single line (list is the parameter)
cities=["dhaka","narsingdi","savar","rajshahi","chittagong"]
heros=["thor","iron man","captain america"]
list1=[1,2,3,4,5,6,7]

def print_list (list):
    for el in list:
        print(el,end=" ") #end=" "  is for print the list in the same line


print_list(cities)  
print_list(list1) 
print_list(heros)      
