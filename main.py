# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. \n")
#convert the names from string into list format
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print out the names and count
# print(names)
names_count = len(names)
#introduce ramdomization
# print(names_count)
names_random = random.randint(0, names_count - 1)
who_will_pay = names[names_random]
print("\n" + who_will_pay + ", will pay for every body's food today")




