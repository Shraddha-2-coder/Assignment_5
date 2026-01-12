List = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list:{List}")
count=0
new_list=[]
for i in List:
   new_list.append(i)
   count+=1
   if count==5:
     break
print(f"Extracted first five elements:{new_list}")
reversed_list=[]
for i in range(len(new_list)-1, -1, -1):
    reversed_list.append(new_list[i])
print(f"Reversed  extracted elements:{reversed_list}")