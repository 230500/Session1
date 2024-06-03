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
