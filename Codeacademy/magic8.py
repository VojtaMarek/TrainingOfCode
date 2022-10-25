import random as ran

name = "Vojta"
question = "I will finish this course."
answer = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
random_number = ran.randint(1, 9)

print(name, "asks:", question)
print(random_number)
print(answer[random_number-1])
