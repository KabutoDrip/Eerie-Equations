#Takes problem tier, picks an appropriate equation,
#assigns variable values, returns equations and solutions to generated problem
import random
<<<<<<< HEAD
=======
tier = 3 #variable pulled from game based off score, affects problem difficulty
var1,var2,var3,var4,ans = 0,0,0,0,0
equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
equation_set2 = [f"{var1} + {var2} - {var3} = {ans}", f"{var1} - {var2} + {var3} = {ans}"]
equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
equation_set5 = [f"{var1} x {var2} - {var3} = {ans}", f"{var1} + {var2} - {var3} / {var4} = {ans}"]
>>>>>>> 39fe0842fc35b89706873f629af51dba123d5d21

def main():
  tier = 5 #variable pulled from game based off score, affects problem difficulty
  var1,var2,var3,var4 = variable_maker(tier)
  ans = "wot"
  print(format_picker(tier,var1,var2,var3,var4,ans))

def format_picker (tier,var1,var2,var3,var4,ans):
  if (tier==1):
    equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
    chosen_equation = random.choice(equation_set1)    #chooses random equation as a formatted string from equations set 1
    return chosen_equation
  elif (tier==2):
    equation_set2 = [f"{var1} + {var2} - {var3} = {ans}", f"{var1} - {var2} + {var3} = {ans}",f"{var1}"]
    chosen_equation = random.choice(equation_set2)
    return chosen_equation
  elif (tier==3):
    equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = random.choice(equation_set3)
    return chosen_equation
  elif (tier==4):
    equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = random.choice(equation_set4)
    return chosen_equation
  elif (tier==5):
    equation_set5 = [f"{var1} x {var2} - {var3}", f"{var1} + {var2} - {var3} / {var4}"]
    chosen_equation = random.choice(equation_set5)
    return chosen_equation
  
<<<<<<< HEAD
def variable_maker(tier):
    var1 = 0 
    var2 = 0
    var3 = 0
    var4 = 0
    if tier == 1:
      #1-10
      while var1 < var2:
        var1 = random.randint(0,10)
        var2 = random.randint(0,10)
        var3 = 0
        var4 = 0
      return var1,var2,var3,var4
    elif tier == 2:
      #10-100
      while var3 < var2 + var1:
        var1 = random.randint(0,100)
        var2 = random.randint(0,100)
        var3 = random.randint(0,100)
        var4 = 0
      return var1,var2,var3,var4
    elif tier == 3:
      #1-10
      var1 = random.randint(1,10)
      var2 = random.randint(1,10)
      var3 = 0
      var4 = 0
      return var1,var2,var3,var4
    elif tier == 4:
      #1-50
      var1 = random.randint(1,50)
      var2 = random.randint(1,50)
      var3 = 0
      var4 = 0
      return var1,var2,var3,var4
    elif tier == 5:
      #1-100 all whole numbers.
      var1 = random.randint(1,100)
      var2 = random.randint(1,100)
      var3 = random.randint(1,100)
      var4 = random.randint(1,100)
      return var1,var2,var3,var4
    else:
      print("wot")

main()
=======
  
print(format_picker(tier))
>>>>>>> 39fe0842fc35b89706873f629af51dba123d5d21
