from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input())
marks = [int(Student(*input().split()).MARKS) for i in range(n)]
print(sum(marks) / len(marks))