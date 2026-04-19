#Task1: student grading system
#This code takes student name and marks of 5 subjects and calculate tptal,percentage and grade
def calculategrade(p):
    if p >= 90:
        return 'A'
    elif p >= 80:
        return 'B'
    elif p >= 70:
        return 'C'
    elif p >= 60:
        return 'D'
    else:
        return 'F'
s_name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(mark)
total = sum(marks)
p = (total/500)*100
grade = calculategrade(p)
print("\n" + "="*40)
print(f"Student Name: {s_name}")
print(f"Total Marks: {total}/500")
print(f"Percentage: {p:.2f}%")
print(f"Grade: {grade}")
print("="*40)