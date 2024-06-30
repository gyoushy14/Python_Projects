from abc import ABCMeta , abstractclassmethod
# => abc : abstract base classes , ABCMeta : class using for define abc , abstractclassmethod : decorator indicating abstract class method
# BASE CLASS
class Character(metaclass=ABCMeta):
    def __new__(cls,name, alignment,power_level):
        if int(power_level)>=500 and int(power_level)<=1000:
            print("Power Level : Strong Character")
        elif int(power_level)<100 and int(power_level)<=500:
            print("Power Level : Normal Character")
        elif int(power_level)>1000:
            print("Power Level : Master of the Universe")
        return super().__new__(cls)
    def __init__(self, name, alignment,power_level):
        self.name=name
        self.alignment=alignment
        self.power_level=power_level
    @abstractclassmethod
    def definding(self):
        pass
    @abstractclassmethod
    def attacking(self):
        pass
    @abstractclassmethod
    def special_abilities(self):
        pass
    def battle(self):
        pass
# -----------------------------------------------------------------------------------------------------------------------------------
# HEROS CLASS
class heros(Character):
    def __init__(self, name, alignment, power_level):
        super().__init__(name, alignment, power_level)
    def attacking(self):
        print(f"""{self.name} can attack by Laser from his eyes 💥. And Very fast""")
    def definding(self):
        print(f"{self.name} can defindenig by his Shield 🛡️\nif his sheld was damaged , he can run away 🏃‍♂️.")
    def Hero_or_vilain(self):
        if self.alignment=="hero":
            print(f"Name : {self.name}")
            print("ًWelcome Our Hero 🦸🏻‍♂️")
    def special_abilities(self):
        print( "Characters can Fly 🛫")
        return f"{self.name} can control gravity and Very fast like flash"
print("First Character")
btata_man=heros(input("Enter Your Name : "),input("Hero OR Villain ? ").lower(),input("What is Your Power Level ? "))
EL3nabi=heros("el3nabi","hero",4000)
btata_man.Hero_or_vilain()
btata_man.attacking()
btata_man.definding()
list_heros=[btata_man,EL3nabi]
dict_heros={
    "Batata Man" : "Fav Hero",
    "El3Nabi" : "Strongest Hero"
}
# -----------------------------------------------------------------------------------------------------------------------------------
# VILLAINS CLASS
class villains(Character):
    def __init__(self, name, alignment, power_level):
        super().__init__(name, alignment, power_level)
    def Hero_or_vilain(self):
        if  self.alignment =="villian":
            print(f"Name : {self.name}")
            print(f" {self.name} has come to damage Earth ☠️")
    def attacking(self):
        print(f"He can destroy many of plants by on punch 👊👊\nHe has a large army ready to destroy the Earth planet 💥 ")
    def definding(self):
        print(f"He has alot of definding ways. one of strongest way is Electromagnatic field and can damage anything touch it 🤯🤯")
    def special_abilities(self):
        print( "Characters can Fly 🛫")
        return f"{self.name} can control fire and Time"
print("Seconed Character")
Zogdo=villains(input("Enter Your Name : "),input("Hero OR Villain ? ").lower(),input("What is Your Power Level ? "))
Madara=villains("madara","villain",3200)
Zogdo.Hero_or_vilain()
Zogdo.attacking()
Zogdo.definding()
list_villain=[Zogdo,Madara]
dict_villain={
    "Zogdo" : "The king of villains",
    "Madara" : "The ghost of uchiha"
}
# -----------------------------------------------------------------------------------------------------------------------------------
class fight(villains,heros):
    def __init__(self, name, alignment, power_level):
        super().__init__(name, alignment, power_level)
    def battle(self):
        print(f"Abilities Of {Zogdo.name} :\n {Zogdo.special_abilities()} 🔥 Power Level : {Zogdo.power_level}")
        print(f"Abilities Of {btata_man.name} :\n {btata_man.special_abilities()} ⚡️ Power Level : {btata_man.power_level}")
        print(f"Start of the warrior between iur hero {btata_man.name} and villain has come to damage Earth {Zogdo.name} ⚔️")
        if int(Zogdo.power_level) > int(btata_man.power_level):
            print(f"Zogdo and his army came to Earth and our heroes confronted them, but unfortunately our heroes were unable to do anything against them because of their great strength and large numbers. The {Zogdo.name} wins and destroys planet Earth")
        elif int(Zogdo.power_level) < int(btata_man.power_level):
            print(f"After the battle began, which continued for a long time, Using Btata Man's special abilities, he was able to eliminate Zogdo. The {btata_man.name} wins and peace returns again to our planet")
        elif int(Zogdo.power_level) == int(btata_man.power_level):
            print(f"After a long, epic battle that caused damage to both sides, Zogdo decided to retreat now to re-strengthen himself and his army. Btataman took advantage of the retreat by evacuating the citizens and preparing for war again")
obj=fight("","",0)
obj.battle()