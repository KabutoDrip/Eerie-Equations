#Takes problem tier, picks an appropriate equation,
#assigns variable values, returns equations and solutions to generated problem
import random
tier = 1
var1,var2,var3,var4,ans = 0,0,0,0,0
equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
equation_set2 = [f"{var1} + {var2} - {var3} = {ans}", f"{var1} - {var2} + {var3} = {ans}",f"{var1}"]
equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set5 = [f"{var1} x {var2} - {var3}", f"{var1} + {var2} - {var3} / {var4}"]

def format_picker (tier):
  if (tier==1):
    chosen_equation = random.choice(equation_set1)
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
  
  
format_picker(tier)