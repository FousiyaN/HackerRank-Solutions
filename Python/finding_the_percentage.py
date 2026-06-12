import math
n = int(input(""))
student = {}
for i in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float,data[1:]))
    
    student[name]=marks
query = input("")
marks = student[query]
    
average = sum(marks)/len(marks)
print(f"{average:.2f}")
    
    
