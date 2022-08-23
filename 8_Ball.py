import random

name = "Kuba"
question = "" 
answer = ""
random_number = random.randint(1,11)

print(random_number)

if random_number == 1:
 answer += "Yes definitely."
elif random_number == 2:
 answer += "It is decidely so."
elif random_number == 3:
 answer += "Without a doubt."
elif random_number == 4:
 answer += "Reply hazy, try again."
elif random_number == 5:
 answer += "Ask again later."
elif random_number == 6:
 answer += "Better not tell you now."
elif random_number == 7:
 answer += "My sources say no."
elif random_number == 8:
 answer += "Outlook not so good."
elif random_number == 9:
 answer += "Very doubtful."
elif random_number == 10:
 answer += "I love that."
elif random_number == 11:
 answer += "That is possible."
else:
 print ("Error")

if name == "" and question == "":
   print ("Please ask question.")
elif name == "": 
 print ("Question: " + question +  " \nMagic 8-Ball's answer: " +  answer)
elif question == "":
  print (name + ". Please ask question")
else:
 print (name + " asks: " + question + " \nMagic 8-Ball's answer: " + answer)