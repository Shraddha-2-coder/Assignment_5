

📌 Program 1: Student Marks Lookup Using Dictionary

🔹 Description

This program stores student names and their marks in a dictionary. The user enters a student name, and the program displays the corresponding marks if the student exists. Otherwise, it shows an appropriate message.

⸻

🔹 Concepts Used
	•	Dictionary (key–value pairs)
	•	User input
	•	Conditional statements (if-else)
	•	Membership operator (in)
	•	Formatted output (f-string)

⸻

🔹 Code

students = {
    "Shraddha": 97,
    "Shreya": 88,
    "Monika": 50,
  
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")


⸻

🔹 Sample Input

Enter the student's name: Shraddha

🔹 Sample Output

Shraddha's marks: 97


⸻

🔹 Use Case
	•	Quick data lookup
	•	Student management basics
	•	Understanding dictionaries in Python

⸻

📌 Program 2: Extract and Reverse First Five Elements of a List

🔹 Description

This program takes a list of numbers, extracts the first five elements, and then reverses those extracted elements using loops.

⸻

🔹 Concepts Used
	•	Lists
	•	for loop
	•	break statement
	•	List indexing
	•	List reversal logic

⸻

🔹 Code

List = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {List}")

count = 0
new_list = []

for i in List:
    new_list.append(i)
    count += 1
    if count == 5:
        break

print(f"Extracted first five elements: {new_list}")

reversed_list = []
for i in range(len(new_list)-1, -1, -1):
    reversed_list.append(new_list[i])

print(f"Reversed extracted elements: {reversed_list}")


⸻

🔹 Sample Output

Original list: [1,2,3,4,5,6,7,8,9,10]
Extracted first five elements: [1,2,3,4,5]
Reversed extracted elements: [5,4,3,2,1]


⸻

🔹 Use Case
	•	Understanding list traversal
	•	Practicing indexing
	•	Learning manual reversal logic (important for exams)

⸻

