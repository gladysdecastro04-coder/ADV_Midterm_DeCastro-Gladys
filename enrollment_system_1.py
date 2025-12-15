print("=== ENROLLMENT SYSTEM ===")

full_name = input("Enter Full Name: ")
address = input("Enter Address: ")
age = input("Enter Age: ")

courses = ["BSIT", "BSCS", "BSIS"]

print("\nAvailable Courses:")
for i, course in enumerate(courses, 1):
    print(f"{i}. {course}")

course_choice = int(input("Select course (1-3): "))
selected_course = courses[course_choice - 1]

num_subjects = int(input("Enter number of subjects: "))
rate_per_subject = 1500

total_payment = num_subjects * rate_per_subject

print("\n=== ENROLLMENT SUMMARY ===")
print("Student Name:", full_name)
print("Address:", address)
print("Age:", age)
print("Course:", selected_course)
print("Number of Subjects:", num_subjects)
print("Total Payment: PHP", total_payment)
