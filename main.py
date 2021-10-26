import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
options = ("Banana Bread, Chocolate chip cookies, Chocolate cake, Red velvet cake, Apple pie, Cherry pie")


name=input('Hello friend what is your name? -------------You:')
print(f'Well hellooo {name} I am Archie, what recipes would you like to explore today? We have Banana bread, Chocolate chip cookies, Chocolate cake, Apple pie, Red velvet cake, and Cherry pie as todays menu --------------  You:')

assist=input()
print(f'Well ok I can look and see if I have {assist} for you...............')
print("----------------------------------------")

#options 
if (assist) == 'Banana bread':
  print("'Ripe bananas, 'Flour', 'Butter', 'Eggs', 'Baking Powder','Sugar', 'Walnut', 'Brown Sugar','Ground Cinnamon' are all of the ingredients for banana bread")



elif(assist) == 'Chocolate chip cookies':
  print("'Chocolate chips', 'Butter', 'Sugar', 'Flour', 'Egg', 'Brown Sugar', 'Vanilla', 'Unsalted Butter' are all of the ingredients for chocolate chip cookies")



elif(assist) == 'Chocolate cake':
  print(" 'Chocolate', 'Cream', 'Egg', 'Butter', 'Flour', 'Cocoa soilds', 'Vanilla', 'Baking powder', 'Sugar', 'Buttermilk', 'Unsalted butter' are the ingredients for Chocolate cake.")



elif(assist) == 'Red velvet cake':
  print("'Cream cheese', 'Butter', 'Vanilla', 'Flour', 'Red food coloring', 'Buttermilk', 'Egg', 'Sugar', 'Cocoa solids', 'Powdered Sugar', 'Baking Powder', 'Vanilla extract', 'All purpose flour', 'Unsalted butter' are the ingredients for Red velvet cake.")

elif (assist) == 'Apple Pie':
  print("'Apples', 'Butter', 'Flour', 'Egg', 'Cinnamon', 'Crust', 'Sugar', 'Brown Sugar', 'Juice' are the ingredients for Apple pie.") 



elif (assist) == 'Cherry Pie':
  print("'Cherries', 'Crust', 'Sour cherries', 'Butter', 'Flour', 'Sugar', 'Egg', 'Lemon', 'Corn Starch' are the ingredients for Cherry pie.")


else:
  print("I am sorry I don't have that on today's menu")



