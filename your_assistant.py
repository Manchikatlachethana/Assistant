import time,datetime

name=input('Enter your name:')
print('Hi',name)
user_ans=input('How are you today? Good or Bad:')

#if its Good from user:
if user_ans=='Good':
	time.sleep(1)
	print("That's happy to hear from you...")
	time.sleep(2)
	print('Now,lets start programming and learn more!')
	time.sleep(2)
	print("""Work Hard! Push yourself to do more...""")
	print('Happy',datetime.date.today().strftime('%A'),'!',name)

#if its Bad from user:
if user_ans== "Bad":
	time.sleep(1)
	print("Okay, Listen to me now...")
	time.sleep(3)
	print("Listen",name,",you have only fews holidays left to learn and not even one best project with you,")
	print("and you're telling me that today you'll not program?")
	time.sleep(4)
	print('see,its',datetime.date.today().strftime('%A'),'the',datetime.date.today().strftime('%w'),'nd day of the week')
	print("->Don't be a loser and don't tell that you're not good enough. COME ON...",name)
	time.sleep(4)
	print("What do you think? people like Steve Jobs, Bill gates and Elon Musk are born with talent?")
	time.sleep(4)
	print("NOOO... they work hard for it not like you",name,"and they are always willing to work hard even more than you",name)
	time.sleep(4)
	print("In life there's not talent ,there's only HARDWORK and SKILLS, and you may ask me that how to get skills?")
	time.sleep(4)
	print("By WORKING HARD everyday on thing you like, WORK LIKE HELL IF YOU WANT TO IMPROVE")
	time.sleep(3)
	print("People like you(", name ,") will lose, if you don't change your mindset, YOU HAVE TO BELIEVE IN YOURSELF")
	time.sleep(4)
	print("BE TOUGH, BE STRONG, BE HUNGRY, BE STUDENT buddy!")
	time.sleep(3)
	print("""BE STUDENT MEANS:
		>Live like student, always LEARNING:)
		>DREAMS COME TRUE!
		>WORK HARD PAYS OFF!
		-->ALWAYS REMEMBER THAT!<---""")
