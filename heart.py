
def heart():
 for row in range(6):
   for col in range(7):
     if((row==0 and col%3!=0) or
       (row==1 and col%3==0)or 
       (row-col==2)or
       (row+col==8)):
       print("*",end=" ")

     else:
        print(" ",end=" ")

   print()



def triangle():
  for i in range(1,6):
    for j in range(i):
        print("*",end="")
 
    print()



def opp_triangle():
  for i in range(5,0,-1):
    for j in range(i):
      print("*",end=" ")
    
    print()

def square():
  for i in range(5):
    for j in range(5):
      print("*",end=" ")

    print()

while True:
  print("1. Heart")
  print("2. Triangle")
  print("3. Opposite Triangle")
  print("4. Square")
  print("5. Exit")

  choice = int(input("Enter your choice:="))

  if choice==1:
    heart()
  elif choice==2:
    triangle()
  elif choice==3:
    opp_triangle()
  elif choice==4:
    square()
  elif choice==5:
    break