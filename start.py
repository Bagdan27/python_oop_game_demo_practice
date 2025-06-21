# базовые классы
class Backpack:
   def __init__(self, strength, weight):
       self.strength = strength
       self.weight = weight


class Weapon:
   def __init__(self, type, weight):
       self.type = type
       self.weight = weight


class Gun(Weapon):
   def __init__(self, type, weight):
       super().__init__(type, weight)


class Bullets(Weapon):
   def __init__(self, type, weight):
       super().__init__(type, weight)


class Equipment:
   def __init__(self, category, weight):
       self.category = category
       self.weight = weight


class Player:
   def __init__(self, name, carrying, speed, backpack=None, bullets=None):
       self.name = name
       self.carrying = carrying
       self.speed = speed
       self.backpack = backpack
       self.gun = None
       self.bullets = bullets
       self.equipment = []


# выбор рюкзака
   def choose_backpack(self, choice):
       if choice == 1:
           self.backpack = Tactic
           print(f"You chose Tactic - strength: {self.backpack.strength}, weight: {self.backpack.weight}")
       elif choice == 2:
           self.backpack = Basic
           print(f"You chose Basic - strength: {self.backpack.strength}, weight: {self.backpack.weight}")
       elif choice == 3:
           self.backpack = Special
           print(f"You chose Special - strength: {self.backpack.strength}, weight: {self.backpack.weight}")
       else:
           print("Wrong input")
           return False
       return True


# выбор оружия
   def choose_gun(self, choice):
       if choice == 1:
           self.gun = glock
           print(f"You chose Glock - type: {self.gun.type}, weight: {self.gun.weight}")
       elif choice == 2:
           self.gun = ak47
           print(f"You chose AK47 - type: {self.gun.type}, weight: {self.gun.weight}")
       elif choice == 3:
           self.gun = bow
           print(f"You chose Bow - type: {self.gun.type}, weight: {self.gun.weight}")
       else:
           print("Wrong input")
           return False
       return True


# выбор пуль
   def choose_bullet(self, choice):
       if choice == 1:
           self.bullets = pistol_bullets
           print(f"You chose pistol bullets")
       elif choice == 2:
           self.bullets = rifle_bullets
           print(f"You chose rifle bullets")
       elif choice == 3:
           self.bullets = arrows
           print(f"You chose arrows")
       else:
           print("Wrong input")
           return False
       return True


# выбор инвентарь
   def choose_equipment(self, choice):
       equipment_list = [torch, clothes_for_cold, clothes_for_warm, lighter_gas, lighter_electric, rope, knife]
       if choice < 1 or choice > len(equipment_list):
           print("Wrong input")
           return False
       selected = equipment_list[choice - 1]
       if selected in self.equipment:
           print(f"You already have {selected.category}")
           return False
       self.equipment.append(selected)
       print(f"You added {selected.category} - weight: {selected.weight}")
       return True


# проверка веса
   def check_weight(self):
       total_weight = 0
       if self.backpack:
           total_weight += self.backpack.weight
       if self.gun:
           total_weight += self.gun.weight
       if self.bullets:
           total_weight += self.bullets.weight
       for item in self.equipment:
           total_weight += item.weight
       if total_weight > self.carrying:
           print(f"Warning: Total weight ({total_weight:.2f}) exceeds carrying capacity ({self.carrying})! Your speed is reduced.")
           self.speed = max(1, self.speed - int(total_weight - self.carrying))
           return False
       return True


# вспомогательный функциноал
def display_current_weight(player):
   content_weight = 0
   backpack_weight = player.backpack.weight if player.backpack else 0
   if player.gun:
       content_weight += player.gun.weight
   if player.bullets:
       content_weight += player.bullets.weight
   for item in player.equipment:
       content_weight += item.weight
   total_weight = content_weight + backpack_weight
   print(f"\nCurrent Weight Status:")
   print(f"- Backpack weight: {backpack_weight:.2f}")
   print(f"- Items weight (gun, bullets, equipment): {content_weight:.2f}")
   print(f"- Total weight: {total_weight:.2f}")
   if player.backpack:
       print(f"- Backpack capacity remaining: {player.backpack.strength - content_weight:.2f}")


# проверка веса с добавлением ++
def check_total_weight_and_proceed(player):
   if not (player.backpack and player.gun and player.bullets):
       print("You must choose a backpack, gun, and bullets!")
       return False


   content_weight = 0
   content_weight += player.gun.weight
   content_weight += player.bullets.weight
   for item in player.equipment:
       content_weight += item.weight


   backpack_weight = player.backpack.weight if player.backpack else 0
   total_weight = content_weight + backpack_weight


   print(f"\nFinal Weight Breakdown:")
   print(f"- Backpack weight: {backpack_weight:.2f}")
   print(f"- Items weight (gun, bullets, equipment): {content_weight:.2f}")
   print(f"- Total weight: {total_weight:.2f}")


   if content_weight > player.backpack.strength:
       print(f"Error: Items weight ({content_weight:.2f}) exceeds backpack capacity ({player.backpack.strength})!")
       print("You need to choose your gear again.")
       player.backpack = None
       player.gun = None
       player.bullets = None
       player.equipment = []
       return False
   else:
       print(f"{player.name} is ready for the adventure!")
       return True


# рюкзаки
Tactic = Backpack(5, 3)
Basic = Backpack(3.5, 1)
Special = Backpack(4, 2.2)
# оружие
glock = Gun("pistol", 1)
ak47 = Gun("rifle", 3)
bow = Gun("stealth", 0.8)
# пули
pistol_bullets = Bullets("pistol", 0.3)
rifle_bullets = Bullets("rifle", 0.5)
arrows = Bullets("stealth", 0.2)
# инвентарь
torch = Equipment("Basic Torch", 1.0)
clothes_for_cold = Equipment("Clothes for Cold", 3.0)
clothes_for_warm = Equipment("Clothes for Warm", 1.5)
lighter_gas = Equipment("Gas Lighter", 0.5)
lighter_electric = Equipment("Electric Lighter", 0.5)
rope = Equipment("Rope", 0.3)
knife = Equipment("Knife", 0.5)


# Логика !!!
player_name = input("Give a name to your character:\n")
player = Player(name=player_name, carrying=9, speed=10)
print(f"Hello, {player.name}!\nHere are your stats:\nCarrying: {player.carrying}\nSpeed: {player.speed}")


while True:
# выбор рюкзак
   while True:
       print("\nNow you must choose your backpack before adventure:\n")
       print(f"Press 1 to choose Tactic - strength: {Tactic.strength}, weight: {Tactic.weight}")
       print(f"Press 2 to choose Basic - strength: {Basic.strength}, weight: {Basic.weight}")
       print(f"Press 3 to choose Special - strength: {Special.strength}, weight: {Special.weight}")
       try:
           choice = int(input("Your choice: "))
           if player.choose_backpack(choice):
               display_current_weight(player)
               break
           print("Please try again with a valid choice.")
       except ValueError:
           print("Invalid input. Please enter a number.")


# выбор оружие
   while True:
       print("\nChoose your gun:\n")
       print(f"Press 1 to choose Glock - type: {glock.type}, weight: {glock.weight}")
       print(f"Press 2 to choose AK47 - type: {ak47.type}, weight: {ak47.weight}")
       print(f"Press 3 to choose Bow - type: {bow.type}, weight: {bow.weight}")
       try:
           gun_choice = int(input("Your choice: "))
           if player.choose_gun(gun_choice):
               display_current_weight(player)
               break
           print("Please try again with a valid choice.")
       except ValueError:
           print("Invalid input. Please enter a number.")


# выбор пули
   while True:
       print("\nChoose bullets for gun:\n")
       print(f"Press 1 to choose bullets for Glock - type: {pistol_bullets.type}, weight: {pistol_bullets.weight}")
       print(f"Press 2 to choose bullets for AK47 - type: {rifle_bullets.type}, weight: {rifle_bullets.weight}")
       print(f"Press 3 to choose arrows for Bow - type: {arrows.type}, weight: {arrows.weight}")
       try:
           bullet_choice = int(input("Your choice: "))
           if player.choose_bullet(bullet_choice):
               display_current_weight(player)
               break
           print("Please try again with a valid choice.")
       except ValueError:
           print("Invalid input. Please enter a number.")


# выбор инвент
   print("\nChoose up to 3 equipment items:\n")
   equipment_list = [torch, clothes_for_cold, clothes_for_warm, lighter_gas, lighter_electric, rope, knife]
   for i, item in enumerate(equipment_list, 1):
       print(f"Press {i} to choose {item.category} (weight: {item.weight})")
   for _ in range(3):
       try:
           equip_choice = int(input("Your choice (0 to skip): "))
           if equip_choice == 0:
               break
           if not player.choose_equipment(equip_choice):
               print("Try again.")
           else:
               display_current_weight(player)
           if len(player.equipment) == 3:
               break
       except ValueError:
           print("Invalid input. Try again.")
   player.check_weight()


# проверка
   if check_total_weight_and_proceed(player):
       print("Proceeding to the adventure")
       break
   else:
       print("\nRestarting gear selection\n")


print(f"\n{player.name}, you are now equipped and ready to explore the dangerous forest!")


