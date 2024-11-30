# 1 Write Python code that prints your name, student number and email address.
print('Thahliya_M')
print('ST_D41_53')
print('thahliyamist@gmail.com')

#  2 Write Python code that prints your name, student number and email address using escape sequences.
print('Thahliya_M\nST_D41_53\nthahliyamist@gmail.com\n')

#  3 Write Python code that add, subtract, multiply and divide the two numbers.
a=14
b=7
print(' 14+7=',a+b,'\n'' 14-7=',a-b,'\n','14*7=',a*b,'\n','14/7=',a/b )

# 4 Write Python code that displays the numbers from 1 to 5 as steps.
print('1\n2\n3\n4\n5\n')

#  5 Write Python code that outputs the following sentence
#  (including the quotation marks and line break) to the screen:
# An example runs of the program: "SDK" stands for "Software Development Kit",
# whereas "IDE" stands for "Integrated Development Environment"
print(' "SDK" stands for "Software Development Kit" ,whereas\n "IDE" stands for "Integrated Development Environment"')

#  6 Practice and check the output print("python is an \"awesome\" language.")
# print("python\n\t2023") print('I\'m from Entri.\b') print("\65") print("\x65")
# print("Entri", "2023", sep="\n") print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# 7 Define the variables below. Print the types of each variable.
# What is the sum of your variables? (Hint: use a type conversion function.)
# What datatype is the sum? num=23 textnum="57" decimal=98.3
num=23
textnum="57"
decimal=98.3
print(type(num))
print(type(textnum))
print(type(decimal))
a=num+int(textnum)+decimal
print('Sum = ',a,'\n' 'Data_type =',(type(a)))


# 8 calculate the number of minutes in a year using variables for each unit of time.
# print a statement that describes what your code does also. Create three variables to
# store no of days in a year, minute in a hour, hours in a day, then calculate the total
# minutes in a year and print the values (hint)
# total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour
num_of_days_in_an_year=365
Minutes_in_an_hour=60
Hours_in_a_day=24
Total_number_of_minutes_in_an_year=num_of_days_in_an_year*Hours_in_a_day*Minutes_in_an_hour
print('This_program_calculates_Number_of_minutes_in_a_year ')
print('Total_number_of_minutes_in_an_year= {} years * {} Hours * {} Minutes'
      .format(num_of_days_in_an_year,Hours_in_a_day,Minutes_in_an_hour))
print(Total_number_of_minutes_in_an_year)

# 9 Write Python code that asks the user to enter his/her name and then output/prints his/her
# name with a greeting. An example runs of the program: Please enter you name: Tony
# Hi Tony, welcome to Python programming :)
Name=input('Please enter your name: ')
print('Hi {},Welcome to Python Programming'.format(Name))



