a=int(input("enter the number in physics"))
b=int(input("enter the number in chemistry"))
c=int(input("enter the number in biology"))
d=int(input("enter the number mathematics"))
e=int(input("enter the number computer"))
percentage=a+b+c+d+e/500*100
if (percentage>=90):
                  print("grade A")
elif (percentage>=80):
                 print("grade B")
elif (percentage>=70):
                print("grade C")
elif (percentage>=60):
                print("grade D")
elif (percentage>=50):                
               print("grade E")
elif (percentage<40):
              print("grade F")
else:
       print("you are fail")
       

