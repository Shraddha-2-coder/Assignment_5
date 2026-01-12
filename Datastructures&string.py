dict =  {
    "Shraddha": 95,
    "Shreya": 88,
    "Monika": 50,
    "Liza" : 81,

}
name=input("Enter the  student's name : ")
if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("student not found")