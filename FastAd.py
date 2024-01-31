#This is a script that you can use to calculate the expected return of Fast Adaptation from a given base hit chance.
#The only value you should edit is the value BASE_HIT_CHANCE. Everything else can be left alone.
#If you want to see the rolls appended to a file then you can remove the #comment in front of lines 15,20, and 33.

import random
import statistics
import collections

BASE_HIT_CHANCE = 40

data_list = []

current_hit_chance = BASE_HIT_CHANCE

#f = open("FastAd.txt","w")

for i in range(0,1000000):
    roll = (random.randint(1,100))
    data_list.append(current_hit_chance)
    #f.write(str(current_hit_chance)+ "\n")
    if roll > current_hit_chance:
        current_hit_chance += 10
        if current_hit_chance > 95:
            current_hit_chance = 95
    else:
        current_hit_chance = BASE_HIT_CHANCE

Avg_Hit_Chance = statistics.mean(data_list)
Counter_for_Rolls = collections.Counter(data_list)
Percentage_of_Rolls_at_Each_Hit_Value = [(i,Counter_for_Rolls[i]/len(data_list)*100) for i in Counter_for_Rolls]
print("Average hit chance: " + str(Avg_Hit_Chance))
print("% of rolls at each hit%: " +str(Percentage_of_Rolls_at_Each_Hit_Value))
#f.close()

#Author: turtle225