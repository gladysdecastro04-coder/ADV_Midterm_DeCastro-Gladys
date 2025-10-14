name = input("Enter student names: ")
address = input ("Enter Address: ")
age = input ("Enter Age: ")
print("\nAvailable Courses:")
print("1. BSIT")
print("2. BSCS")
print("3. BSECE")
course_choice = input("Select course (1-3): ")
if course_choice =="1":
    course = "BSIT"
elif course_choice =="2":
    course = "BSCS"
elif course_choice =="3":
    course = "BSECE"
else: 
    course ="Unknown"
print("\nSubject available (each subject =₱1500):")
print ("1. Programming")
print ("2. Networking")
print ("3. web Dev")
subjects = input ("Enter chosen subjects (comma-separated numbers, e.g 1,2):").split(",")
rate = 1500
total_payment = len(subjects) * rate
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Total Subjects: {len(subjects)}")
print(f"Total Payment: ₱{total_payment}")
# Minor update for feature branch
