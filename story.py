"""
from start import (
   Player, Tactic, Basic, Special, glock, ak47, bow,
   pistol_bullets, rifle_bullets, arrows,
   torch, clothes_for_cold, clothes_for_warm, lighter_gas,
   lighter_electric, rope, knife,
   display_current_weight, check_total_weight_and_proceed
)
"""
print("You are going throw the forest, and see the river but it's dangerous."
     "\n Drink water? print 1 or 2 ")


x = int(input())
def water (x):
   if x == 1:
       print ("you drank some water ")
   elif x == 2:
       print ("You didnt drank")


print (water(x))