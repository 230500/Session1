# Part A: Decision-Making with conditional statement
# Topic: The IF-Statement

age = int(input("Enter age: "))
name = str(input("Enter name: "))
if age >= 18:                            #age is a dependant variable
    print("You are an adult", name)
else:
    print("You are a minor", name)



# While LOOP
# Topic: The While Loop (Conditioned_Controlled)
count = 1                             # Assigning count as 1.
while count <=5 :                     # Using while condition loop and checking if its less than or equal to 5 (if true it print the frist output), in this case it's 1.
    print(f"Counting.....{count}")    # Using "printf" to print {count} and after that
    count += 1                        # Increment Count is executed and the count value (1) is increased by "+1" for the next loop.



# Continents
continents = ["Asia", "Africa", "Australia", "Europe", "Antartica", "South America", "North America"]      #Assigning continent with the names of all the seen continents
for continents in continents:
    print(f"The names of all the continents is {continents}")

# I am from this continent
continents = ["Asia", "Africa", "Australia", "Europe", "Antartica", "South America", "North America"]      #Assigning continent with the names of all the seen continents
home = "Asia"                            # Assigning home as Asia
for continents in continents:            # Using for loop for continents from continents subset
    print(f"I am from {home}")           # Printing "home" as a print statement

#Topic: Calculating a running total
total = 0                  # Using total and assigning value as "0".
for num in range(1,6):     # using range between number 1 and 6.
    total += num           # Using increment operator to increase the value of total (which was intially "0") in range from 1 to 6.
    print(f"The current total is: {total}")  # this statement will print (0+1) which is 1 and then the for loop will execute again to give total = 1+ 2 = 3.



# I am from this continent
continents = ["Asia", "Africa", "Australia", "Europe", "Antartica", "South America", "North America"]      #Assigning continent with the names of all the seen continents
home = "Asia"                            # Assigning home as Asia
for continents in continents:            # Using for loop for continents from continents subset
    print(f"I am from {home}")           # Printing "home" as a print statement




#Topics: Sentinels (Loops Termination with a Specific Value
number = 0         # Assigning number initially as zero "0".
while number != -1:       # using while loop until user gives input number as -1.
    number = int(input("Enter any number(or -1 to quit):"))     # Asking user to input an integer as an input. or simply put -1 to quit.
    if number != -1:           # check condition if the input number is not equal to -1 then we execute the print statement below to print the entered number by the user.
        print(f"The result is: {number}")



