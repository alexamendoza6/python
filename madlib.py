answer=input("Welcome! Would you like to play Mad Libs?")
if answer=="yes":
	answer=input("Great! Type E for Easy, M for Medium, and H for Hard.")
if answer=="E":
	noun=input("give me a noun:")
	adjective=input("give me an adjective:")
	place=input("give me a place:")
	animal=input("give me an animal:")
	celebrity=input("give me a celebrity:")
	print("once upon a time the "+adjective+" "+noun+" was walking to"+place+", then "+noun+" ran into "+celebrity+" and their pet"+animal)
elif answer=="M":
	noun=input("give me a noun:")
	noun2=input("give me a second noun:")
	adjective=input("give me an ajective:")
	adjective2=input("give me another adjective:")
	verb=input("give me a verb with an 'ing' ending:")
	animal=input("give me an animal:")
	verb2=input("give me a verb:")
	place=input("give me a place:")
	print(noun+" and his sister "+noun2+ " were " +verb+ "to the store. Suddenly, they saw a "+adjective+adjective2+animal+" and "+verb2+" "+place)
elif answer=="H":
	print("welcome to Starbucks!")
	name1=input("what is your name?")
	print("how may I help you "+name1)
	drink1= input("what drink would you like?")
	print("Anything else?")
	adjective=input ("What adjective do you want?")
	print("can I get " +adjective +" sprinkles?")
	price=input("what is the price?")
	print("that will be" +price)
	print("okay, can I add a cookie?")
	price2=input("that will be, how much?")
	print("okay " +name1+ ",that will be"+ price2)
	print("Thank You!")