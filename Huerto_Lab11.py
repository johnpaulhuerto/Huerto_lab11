all_grades = []
succesful_students = []

while True:
    grade_input = input("Please enter a grade (or type 'finish' to end): ")
    
    if grade_input.lower() == 'finish':
        break
    
    if not grade_input.isdigit():
        print("Invalid input: Please enter a number.")
        continue
    
    else:
        grade = int(grade_input)
        
        if grade < 40 or grade > 100:
            print("Error: Grade must be between 40 and 100.")
            continue
        
        else:
            all_grades.append(grade)                       
            if grade >= 75:
                succesful_students.append(grade)
                         
            avg_grade = sum(all_grades) / len(all_grades)
            success_rate = (len(succesful_students) / len(all_grades)) * 100
            print(f"The average grade is: {avg_grade:.2f}")
            print(f"Pass rate: {success_rate:.2f}%")
            print(f"Total number of passing students: {len(succesful_students)}")
            print(f"Grades entered: {all_grades}\n")
   
            if not all_grades:
                print("No valid grades were recorded.")                       