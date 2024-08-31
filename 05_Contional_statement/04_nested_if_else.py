marks = int(input("enter your marks : "))
gender = input("your gender enter male / female :")

if ((marks >= 90)):
    if (gender == "male"): 
        print("A Grade")
        print("You can do better")
    else:
        print("A Grade")
        print("well done")
elif ((marks <= 90) and (marks >=80)):
    if (gender == "male"): 
        print("B Grade")
        print("You can do better")
    else:
        print("B Grade")
        print("well done")
elif ((marks <= 80) and (marks >=70)):
    if (gender == "male"): 
        print("C Grade")
        print("You can do better")
    else:
        print("C Grade")
        print("well done")
elif ((marks <= 70) and (marks >=60)):
    if (gender == "male"): 
        print("D Grade")
        print("You can do better")
    else:
        print("D Grade")
        print("well done")
elif ((marks <= 60) and (marks >=50)):
    if (gender == "male"): 
        print("E Grade")
        print("You can do better")
    else:
        print("E Grade")
        print("well done")
elif ((marks <= 50) and (marks >=40)):
    if (gender == "male"): 
        print("E- Grade")
        print("You can do better")
    else:
        print("E- Grade")
        print("well done")
else:
    print("Fail")