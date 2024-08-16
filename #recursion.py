#recursive function
def show(n):
   if(n == 0): #base case 
      return 
   print(n) 
   show(n-1)
   print("end")
show(5)   