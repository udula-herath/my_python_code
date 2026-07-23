print("______Movie Ticket Price Calculator_____")

age=int(input("How old are you:"))
if age <= 12:
    print("The ticket is free")
elif age <= 18:
    print("A ticket is 500 rupees")
elif age <= 60:
    print("A ticket is 1000 rupees")
else:
    print("A ticket is 300 rupees")

print("_____Student Exam Grading System______")

marks=int(input("what is the maths score?:"))
if marks >= 75:
    print("Grade 'A' ")
elif marks >= 65:
    print("Grade 'B'")
elif marks >= 55:
    print("Grade 'C'")      
elif marks >= 35:
    print("Grade 'S'")      
else:
    print("grade 'F'")    
