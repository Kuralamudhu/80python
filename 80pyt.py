surf=input()
for j in range(0,len(surf)):
   if(surf[j].isalpha() and surf[j].isdigit()):
    print("No")
else:
  print("Yes")
  
