# Activity – 1:
# Write a python program that has a list of even numbers up to 20. Display the first 3 elements
# from the list one by one, then display all numbers in the list, using range function.
# Extend your program to display an average of the given even numbers in the list.
# Answer:

e_ns = list(range(2,22,2))  # Here, "e_ns" is the denotation for list of even numbers.
                           # " list command is used for listing those even numbers.
                           # " range (2,22,2) is range of numbers starting from 2 ends at 22 by stepping 2.
print("The 3 elements at the beginning of lists are:")  # Printing first 3 elements in the list.
for i in range(3):          # Using for loop with range 3 to print first 3 elements in the list.
   print(e_ns[i])          # using e_ns list and for loop that iterates 3 times printing first 3 elements.
print("Remaining even numbers from the list are: ")
for re_n in e_ns:         # Using for loop to print remaining all elements assigned as "re_n" from the list "e_ns".
       print(re_n)       # printing "re_n"
av_g= sum(e_ns)/len(e_ns)  # Assigning average of all numbers as "av_g"
                          # "Sum" is sum of all elements and "len" counts all the element in the list.
print("The Average of all even numbers:", av_g) # print the average of all elements in the list.



# Activity – 2:
# Write a python program that has a list of 5 numbers [1,2,3,4,5]. Print the first 3 elements from
# the list using slice expression.
# Extend this program in a manner that the elements in the list are changed to [2,4,6,8,10] that
# means each element is times 2 of the previous value.
# Extend your program to display the min and max value in the list.

# Answer:

lst = [1, 2, 3, 4, 5]    # Assigning "lst" as a list of numbers containing [1,2,3,4,5] numbers.
print("First 3 expressions after slicing are:", lst[:3])   # "lst[:3]" command prints up to 3 elements in the given "lst".
n_lst = [2 * x for x in lst]     # "n_lst" is the new list assigned to multiply (*2) the original value of the list and replaced with new ones.
print("The new numbers in the list are:", n_lst)   # Printing new values in the "n_lst" list whcih will be [2,4,6,8,10]
mi_n = min(n_lst)                 # "mi_n" to calculate minimum value from the new list.
ma_x = max(n_lst)                 # "ma_x" to calculate maximum value from the new list.
print("The maximum value is: ", ma_x)   # to print maximum value from the new list.
print("The minimum value is: ", mi_n)   # to print minimum value from the new list.




# Activity – 3:
# Write a python program that has four lists:
# summer = ['Dec', 'Jan', 'Feb']
# autumn = ['Mar', 'Apr', 'May']
# winter = ['Jun', 'Jul', 'Jul', 'Aug']
# spring = ['Oct', 'Nov']
# First, remove the excess month ‘Jul’ from the list winter and add month ‘Sep’ at the beginning
# of the spring list.
# Then, make two new lists: MonthsISleep and MonthsIParty, copying the appropriate parts from
# the existing lists so that the list MonthsISleep contains all the months from ‘Feb’ to ‘Nov’ and
# the second list MonthIParty contains the remaining 2 months.
# − Display elements form both lists: MonthsISleep and MonthsIParty.
# − Display the elements of list summer in reverse order
# Answer:

Summer = ['Dec', 'Jan', 'Feb']          # Assigning 1st, 2nd, 3rd and 4th list of months.
Autumn = ['Mar', 'Apr', 'May']          # '' as summer, autumn, winter and spring respectively.
Winter = ['Jun', 'Jul', 'Jul', 'Aug']   # Here, in winter we have 2 "july" so we will need to remove one "july".
Spring = ['Oct', 'Nov']
Spring.insert(0, 'Sep')     # we used "spring.insert" to add "sep" month in Spring month.
Winter.remove('Jul')                        # We used "Winter.remove" to remove one "July" from Winter month.
MonthsIParty = Summer[:-1]                  # Assigning new month as "MonthsIParty"  that will display "Dec" and "Jan".
MonthsISleep = Summer[2:] + Autumn + Winter + Spring   # " MonthsISleep that displays all months from....
print("MonthsIParty contains: ", MonthsIParty)         # " "Feb" to "Nov" from all Summer, Winter, Autumn and Winter.
print("MonthsISleep contains: ", MonthsISleep)         # Printing "MonthsISleep" and "MonthsIParty".
rev = Summer[::-1]                                     # Rev = Summer[::-1] will print list of Summer in reverser order.
print("Summer month in reverse order is: ", rev)       # Printing rev.
