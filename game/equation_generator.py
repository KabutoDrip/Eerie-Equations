#Takes problem tier, picks an appropriate equation,
#assigns variable values, returns equations and solutions to generated problem
import random
tier = 3 #variable pulled from game based off score, affects problem difficulty
var1,var2,var3,var4,ans = 0,0,0,0,0
equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
equation_set2 = [f"{var1} + {var2} - {var3} = {ans}", f"{var1} - {var2} + {var3} = {ans}"]
equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set5 = [f"{var1} x {var2} - {var3} = {ans}", f"{var1} + {var2} - {var3} / {var4} = {ans}"]

def format_picker (tier):
  if (tier==1):
    chosen_equation = random.choice(equation_set1)    #chooses random equation as a formatted string from equations set 1
    return chosen_equation
  elif (tier==2):
    chosen_equation = random.choice(equation_set2)
    return chosen_equation
  elif (tier==3):
    chosen_equation = random.choice(equation_set3)
    return chosen_equation
  elif (tier==4):
    chosen_equation = random.choice(equation_set4)
    return chosen_equation
  elif (tier==5):
    chosen_equation = random.choice(equation_set5)
    return chosen_equation
  
  
print(format_picker(tier))