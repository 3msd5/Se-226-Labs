###########################################
#1
name = input("What is your name?\n")
print("Hello "+ name)
number = input("What is your Student ID?\n")
print("Your ID is "+number)

###########################################
#2
var1 = input("Enter first number\n")
var2 = input("Enter second number\n")

sum= (int(var1) + int(var2))
diff= (int(var1) - int(var2))
prod= (int(var1) * int(var2))

print("var1 = ",var1)
print("var2 = ",var2)
print("var1 + var2 = " ,sum)
print("var1 - var2 = " ,diff)
print("var1 * var2 = " ,prod)

###########################################
#3
stdName = input("What is your name?\n")
labGrade = float(input("Enter your Lab Grade?\n"))
midGrade = float(input("Enter your Midterm Grade?\n"))
finalGrade = float(input("Enter your Final Grade?\n"))
lastScore= float((labGrade*25/100)+(midGrade*35/100)+(finalGrade*40/100))

print("Name: " + stdName)
print("Lab Grade: " + str(labGrade))
print("Midterm Grade: " + str(midGrade))
print("Final Grade: " + str(finalGrade))
print("Last Score: " + str(lastScore))

###########################################
#4
print("*\n**\n***\n**\n*")

###########################################
