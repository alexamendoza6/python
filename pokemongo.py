import random
yellow=(255, 255, 0)

class Pokemon_Go():
		def __init__(self, pokemon, name, cp, hp):
			self.pokemon = pokemon
			self.name = name
			self.cp = cp
			self.hp = hp 
		
		def get_status(self):
			print(self.pokemon, self.name, str(self.cp), str(self.hp))
		def rename(self, new_name):
			self.name= new_name
		def increase_cp (self, amount):
			self.cp= self.cp+ amount
			print(self.cp)
		def decrease_cp (self, amount):
			self.cp= self.cp - amount
		def is_attacked(self, damage):
			self.hp= self.hp - damage
			print(self.hp)
		def attack(self, another, attack_strength): 
			success = random.randint(1,2)
			if success == 1:
				print("Your attack failed")
				self.cp = self.cp - 5
			elif success == 2:
				print("your attack was successful")
				attack_strength = attack_strength *1
				self.increase_cp(5)
				another.is_attacked(attack_strength)
			print(self.get_status())

pikachu = Pokemon_Go("pikachu", "pika", 10, 12) 
pikachu.get_status()
piplup =  Pokemon_Go("piplup", "pip", 5,6)
pikachu.attack(piplup, 5)

class Electric(Pokemon):




# exit()