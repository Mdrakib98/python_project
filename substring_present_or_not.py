user=input("enter a string") #edu
ab=input("enter a substring:")#du
cd=""
for i in range(len(user)):
    for j in range(len(ab)):
        if user[i]==ab[j]:
            cd=cd+ab[j]
if cd==ab:
    print("present")
else:
    print("not present")