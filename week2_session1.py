# Part A: Decision-Making with conditional statement
# Topic: The IF-Statement

age = int(input("Enter age: "))
name = str(input("Enter name: "))
if age >= 18:    #age is a dependant variable
    print("You are an adult", name)
else:
    print("You are a minor", name)
