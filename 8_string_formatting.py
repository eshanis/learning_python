name = "Manny"
number = len(name) * 3
print("Hello {}, you lucky number is {}".format(name, number))
print("your lucky number is {number},{name}".format(name = name, number = len(name) * 4))
print("-------------------")
y = "… ".join(["this","is", "a", "phrase", "joined", "by", "dots"])
print(y)

print("------------------")


n = "This is example, of string".split(",")
print(n)

print("--------------------------")
def student_grade(name, grade):
	name = name
	grade = grade
	print("{name} received {grade}% on the exam.".format(name = name, grade = grade))
	return ""
	
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
