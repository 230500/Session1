# Part A: Decision-Making with conditional statement
# Topic: The IF-Statement

# Activity -1:
# Write a python program that will ask the user their age and if the age is less than 18 it will
# print that you are a minor.

age = float(input("Enter age: "))        # Assigning age to input age of the user. (float can be used for floating point precision numbers like age = 16.5)
name = str(input("Enter name: "))        # Assigning name to input the name of the user.
if age >= 18:                            # Age is a dependant variable which will determine the result of IF condition.
    print(f"You are an adult {name}")      # Printing "you are an adult with the user's name" if age>=18
else:
    print(f"You are a minor {name}")       # Else printing "you are a minor with the user's name" if age<18.




# Activity -2:
# Write a python program that will ask the user their age and if the age is less than 18, then if
# the child's age is less than 5 then no ticket price otherwise 1/2 the full price and if the user's
# age is greater than or equal to 18 then full price.

tot_pc = 90
half_price = 90/2
age = int(input("Enter your age: "))
if age < 5:
    print("Enjoy, You can enter for FREE!")
elif age >= 18:
    print(f"Welcome, Your ticket is full price!, It will cost you: {tot_pc}" )
else:
    print(f"Congratulations! you get 50% discount, Your ticket price is: {half_price}")



# Activity -3:
# Write a python program that will ask the user the marks achieved in a subject and your
# program must display the grade according to the following rule:
# a. 0-49 - "FAIL"
# b. 50-64 - "PASS"
# c. 65 - 74 - "CREDIT"
# d. 75-84 - "DIST" and above and equal to 85 - "HD"
#Answer:

grades = {        # Defining a function as "grades" and stating all the range of score with its corresponding category as fail, pass, credit, distinction and high distinction.
    "FAIL": (0, 49),
    "PASS": (50, 64),
    "CREDIT": (65, 74),
    "DISTINCTION": (75, 84),
    "HIGH DISTINCTION": (85, 100),
}

def calcln(scrd):    # Defining a function as "calcln(scrd)" which will take score as one parameter.
    for grd, range in grades.items():  # Defining grd and range inside the grades dictionary i.e, grades{}.
        if scrd >= range[0] and scrd <= range[1]:  #Setting the range for score. Here range(0) and range(1) defines all the range (0,1) from above grades list.
            return grd    # It will compare the value and return "grd" which is define by calcln(scrd) outside the function.
                          # Else it will print "NONE" if it doesnot fall within the given range.
scrd= int(input("Enter your graded Score:"))  #Asking user to input a score to find out the grade.
grd = calcln(scrd)      # Assigning grade "grd" as "calcln(scrd)" function.
print(f"your grade is: {grd}") #Printing "grd" as result.




# Activity -4:
# Answer:


def magc_dt(dd, mm, yy):      # Defining a function called magic date as "magc_dt(dd, mm, yy)" that will take "day as dd", "month as mm" and "year as yy".
       return dd * mm == yy  # when the function is called it will execute the function " dd * mm == yy" and return the value with a print statement.


dd = int(input("Enter the day of your Date of Birth:"))    # Asking users to input the day from the date of birth.
mm = int(input("Enter the month of your Date Of Birth:"))  # Asking users to input a month from date of birth.
yy = int(input("Enter the last two digit of your Birth Year:"))  # Asking user to input the last two digits of their birth year.
if magc_dt(dd, mm, yy):   # Checking the condition from the above defined function ( dd * mm == yy)
   print(f"The given date is magic date")  # If true, print the date as a magic date.
else:
   print("The given date is not magic date")  # Else, print the date is not a magic date.






