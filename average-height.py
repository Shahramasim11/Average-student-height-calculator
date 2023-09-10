student_heights =input("please enter the heights of students with ,: ")
print(f"The heights given are {student_heights}")
new_list = student_heights.split(",")
print(f"The list of heights is {new_list}")
heights_list = [int(height) for height in new_list]
total_heights = sum(heights_list)
for heights in new_list:
    average_height = total_heights/len(heights_list)
print(f"The average height is {average_height}")