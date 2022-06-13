#Takes problem tier, picks an appropriate equation,
#assigns variable values, returns equations and solutions to generated problem
import random

def main():
  tier = 1 #variable pulled from game based off score, affects problem difficulty
  var1,var2,var3,var4 = variable_maker(tier)
  equation, anwser= (format_picker(tier,var1,var2,var3,var4))
  return equation, anwser

def format_picker (tier,var1,var2,var3,var4):
  ans = '?'
  if (tier==1):
    x = random.randint(0,1)
    if x == 0:
      ans = var1 + var2
    else:
      ans = var1 + var2
    equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
    return equation_set1[x], ans
  elif (tier==2):
    equation_set2 = [f"({var1} + {var2}) - {var3} = {ans}", f"({var1} - {var2}) + {var3} = {ans}"]
    chosen_equation = random.choice(equation_set2)
    return chosen_equation, ans
  elif (tier==3):
    equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = random.choice(equation_set3)
    return chosen_equation, ans
  elif (tier==4):
    equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = random.choice(equation_set4)
    return chosen_equation, ans
  elif (tier==5):
    equation_set5 = [f"({var1} x {var2}) - {var3} = {ans}", f"({var1} + {var2}) - ({var3} / {var4}) = {ans}"]
    chosen_equation = random.choice(equation_set5)
    return chosen_equation, ans
  
def variable_maker(tier):
    var1 = 0 
    var2 = 0
    var3 = 0
    var4 = 0
    if tier == 1:
      var2 = 1
      #1-10
      while var1 < var2:
        var1 = random.randint(0,10)
        var2 = random.randint(0,10)
        var3 = 0
        var4 = 0
      return var1,var2,var3,var4
    elif tier == 2:
      var3 = 1
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

def answer():
  correct_answer=1
  return correct_answer
def fake_answer1():
  f_answer1 = 2
  return f_answer1
def fake_answer2():
  f_answer2 = 3
  return f_answer2

main()