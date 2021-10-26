import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
options = ("Banana Bread, Chocolate chip cookies, Chocolate cake, Red velvet cake, Apple pie, Cherry pie")
name=input('Helo friend, What is your name')
print(f'Hello {name} what recipe would you like to search? Here are your {options} for today please put the name of the following')
assist=input()
print(f'Well ok I can look and see if I have {assist} for you...............')
if (assist) == 'Banana bread':
  print("'Ripe bananas, 'Flour', 'Butter', 'Eggs', 'Baking Powder','Sugar', 'Walnut', 'Brown Sugar','Ground Cinnamon' are all of the ingredients for banana bread")

if(assist) == 'Chocolate chip cookies':
  print("'Chocolate chips', 'Butter', 'Sugar', 'Flour', 'Egg', 'Brown Sugar', 'Vanilla', 'Unsalted Butter' are all of the ingredients for chocolate chip cookies")

if(assist) == 'Chocolate cake':
  print(" 'Chocolate', 'Cream', 'Egg', 'Butter', 'Flour', 'Cocoa soilds', 'Vanilla', 'Baking powder', 'Sugar', 'Buttermilk', 'Unsalted butter' are the ingredients for Chocolate cake.")

if(assist) == 'Red velvet cake':
  print("'Cream cheese', 'Butter', 'Vanilla', 'Flour', 'Red food coloring', 'Buttermilk', 'Egg', 'Sugar', 'Cocoa solids', 'Powdered Sugar', 'Baking Powder', 'Vanilla extract', 'All purpose flour', 'Unsalted butter' are the ingredients for Red velvet cake.")

if (assist) == 'Apple Pie':
  print("'Apples', 'Butter', 'Flour', 'Egg', 'Cinnamon', 'Crust', 'Sugar', 'Brown Sugar', 'Juice' are the ingredients for Apple pie.") 

if (assist) == 'Cherry Pie':
  print("'Cherries', 'Crust', 'Sour cherries', 'Butter', 'Flour', 'Sugar', 'Egg', 'Lemon', 'Corn Starch' are the ingredients for Cherry pie.")



