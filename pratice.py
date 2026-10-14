s = "(1+(2*3)+((8)/4))+1"

list = []

for i in s:
    if i == "(":
        count1 = + 1
        print(count1)
        list.append(count1)
    elif i == ")":
        count2 = + 2
        print(count2)
        list.append(count2)        
    else :
        pass


print(list)