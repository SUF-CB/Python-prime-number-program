# Name of program- Prime Numbers
# programmer-Sufyaan Shaikh 
# version 1.0
# Date Created- 12/06/2020
name = input("What's your name?")# First the user will get asked to input their name.
print("Hi, " + name + "! Welcome to your Maths lesson. Today, we are going to be learning about Prime Numbers! This lesson is  a quick check to see if you are ready to master this topic in your exam.")# welcomes user/quick inro
print ("If this is your strength then,this lesson will not waste your time to focus on your weaknesses.")
print (" If this topic is your weakness then, this lesson will refresh your memory on prime numbers")
print("Before we Begin listing the Prime numbers between 1 and 100, Lets First of all see if you know  what a Prime number is")
knowledge = input("Do You what a Prime Number is? Yes or No >> ") # The user will be asked to input eihter Yes/NO if they know what a prime number is.
if knowledge == "Yes":# if the user inputs Yes as their answer it will output the message and praise the user by saying well done along with their  name.
   print("Well done, " + name + "!")
   
else: #  if the user inputs No it will tell the user dont worry and it will provide them with the defintion of a prime number
        print("Dont worry " + name  + "!" " A prime number is a number that has two factors which are one and itself")

prime = input (" Can you list the prime number between 1 and 100? Yes or No >>")# The user will be asked to input eihter Yes/NO if they can list the prime numbers between 1 and 100.

if prime == "Yes": # if the user inputs Yes it will praise the student and output the message well done with the students name, you have completed the lesson and have a nice a day! 
   print("Well done, " + name + "!" "You have now completed the lesson")
   print ("Best of luck in your exam!")
   print ("Enjoy the rest of your day!")
    
   exit() # The user is confident on this topic as they have typed Yes for their answers. Therefore, the program will close automatically with the exit function.
else: # if the user inputs No it will output the message dont worry along with the students name. Below this message it will list the prime numbers between 1 and 100.
        print("Dont worry " + name  + "!" " Here is the list of prime Numbers from 1 to 100 below")
 

 
for num in range(2,100): # A for loop is used here to iterate the numbers which are in range of 2-100 as 1 is not a prime number.
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break #terminates the for loop from running
       else:
           print(num)
print ("Thanks for attending the lesson on prime numbers Best of luck in your exam!")
print ("Enjoy the rest of your day!") 
exit()# The user has now been familiarised with this topic. Therefore, the program will close with the exit function . 



