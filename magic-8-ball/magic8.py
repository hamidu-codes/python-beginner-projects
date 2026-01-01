#This ensures the answer is always randomly chosen each time program is run.
import random

# The lines below prompt the user for input at runtime.
# This improves usability by removing the need to manually edit
# the code for different users or questions.

#Ask user to input their name. Will not proceed until there is a user input.
name = input("What's your name? (Press Enter to skip): ").strip()

#Ask user to input their yes/no question. Will not proceed until there is a user input.
question = input("What's your Yes/No question?: ").strip()

#Reveal answer
answer =("")

#Generate number from 1 to 11
random_number = random.randint(1, 11)

#Possible answers that can be chosen 1 to 11
if random_number == 1:
  answer = ("Yes - definitely")
elif random_number == 2:
  answer = ("It is decidedly so")
elif random_number == 3:
  answer = ("Without a doubt")
elif random_number == 4:
  answer = ("Reply hazy, try again")
elif random_number == 5:
  answer = ("Ask again later")
elif random_number == 6:
  answer = ("Better not tell you now")
elif random_number == 7:
  answer = ("My sources say no")
elif random_number == 8:
  answer = ("Outlook not so good")
elif random_number == 9:
  answer = ("Very doubtful")
#Task 12
elif random_number == 10:
  answer = ("I can’t even answer that!")
elif random_number == 11:
  answer = ("Oh yeah 100%!")

#Else used incase the random.randint exceeds 11. But it cannot unless manually changed, this code should not take effect.
else:
  answer = "Error"

#What happens if user does not input a question.
if question == "":
  print("No question has been given!")

#What happens if no name is entered + what happens if name is entered.
else:
    if name == "":
     print("Question: " + question)
    else:
      print(name + " asks: " + question)
      print ("Magic 8-Ball's answer: " + answer)

