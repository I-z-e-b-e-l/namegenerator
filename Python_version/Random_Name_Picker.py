print("Hello Meow")

# I've never coded in Python before, so I googled each step in the process, starting with "How to create an array in Python." I learned that Python doesn't have arrays, but it does have lists. 

#listofnames = ["Lex", "Lilly", "Nova"]
#print("These are all the items in the list:", listofnames)

#next, how to add items to the list (read up on list methods)

#anothername = "x"

#listofnames.append(anothername)

# print("These are all the items in the list:", listofnames)

#find how to get the length of the list
# print(len(listofnames))

#find how to print different items in the list; seems to work like arrays
# print(listofnames[0])

#find how to generate a random number w/ a min an max. tried several methods that involved a seed but they were not good. this built in function is way easier than what I did in JavaScript

import random

#print(random.choice(listofnames))

#now I'm going to go back to the beginning and see if I can figure out how to get names from the user to append to the list

print("________________")

listofnames = []

newname = input("Please enter a name:\n")
 
#print(f'You entered: {newname}')

listofnames.append(newname)

#print(listofnames)

#that was surprisingly easy. Now I need to figure out how to prompt the user to keep adding names until they are done. Will read up on while loops and whatever the equavalent of functions are

#This works, but gets me a prompt at the very end asking for another name... maybe use break or continue? 

# def add_another_name():
#   anothername = input ("Please enter another name:")
#   listofnames.append(anothername)

#   addmorenames = input("Would you like to add another name? Enter yes or no:")

#   while addmorenames == "yes":
#     add_another_name()
#   else:print("The random name selected is:", random.choice(listofnames))
    
# add_another_name()



#This did not work...

# def add_another_name():
#   anothername = input ("Please enter another name:")
#   listofnames.append(anothername)

#   addmorenames = input("Would you like to add another name? Enter yes or no:")

#   while addmorenames not in ("yes", "no"):
  
#     if addmorenames == "yes":
#       add_another_name()

#     elif addmorenames == "no":
#       print("The random name selected is:", random.choice(listofnames))
  
#     else: 
#       print("Please enter yes or no.") 
  
    
# add_another_name()


#i tried a bunch of things, can't get a break in the while statement if a no is inputted

# def add_another_name():
#   anothername = input ("Please enter another name:")
#   listofnames.append(anothername)

#   addmorenames = input("Would you like to add another name? Enter yes or no:")

#   if addmorenames == "no":
#     print("The random name selected is:", random.choice(listofnames))

#   elif addmorenames == "yes": 
#     while addmorenames == "yes": 
#       add_another_name() 
#       if addmorenames == "no":
#         break
  
    
# add_another_name()

# print("hits the end")

def add_another_name():
  anothername = input ("Please enter another name: ")
  listofnames.append(anothername)

  yesorno = input ("Would you like to add another name? Please enter yes or no: ")

  while True:
    if yesorno == "yes":
      add_another_name()
      break

    if yesorno =="no":
      print(f'The names you entered are: {listofnames}')
      print(f'The random name selected is: {random.choice(listofnames)}')
      break
    
    if yesorno != "no" and yesorno !="yes":
      print("Neither yes or no entered. Please run again.")
      break
  

add_another_name()
