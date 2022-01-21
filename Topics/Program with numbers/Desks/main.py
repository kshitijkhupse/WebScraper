# put your python code here
student_group1 = int(input())
student_group2 = int(input())
student_group3 = int(input())

total_desk_group1 = (student_group1 // 2) + (student_group1 % 2)

total_desk_group2 = (student_group2 // 2) + (student_group2 % 2)

total_desk_group3 = (student_group3 // 2) + (student_group3 % 2)

total_desk = total_desk_group1 + total_desk_group2 + total_desk_group3

print(total_desk_group1 + total_desk_group2 + total_desk_group3)
