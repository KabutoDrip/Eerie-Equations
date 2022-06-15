#Takes problem tier, picks an appropriate equation,
#assigns variable values, returns equations and solutions to generated problem
import random

def main():
  tier = 1 #variable pulled from game based off score, affects problem difficulty
  var1,var2,var3,var4 = variable_maker(tier)
  equation, anwser= (format_picker(tier,var1,var2,var3,var4))
  return equation, anwser

def format_picker (tier,var1,var2,var3,var4):
  if (tier==1):
    x = random.randint(0,1)
    if x == 0:
      ans = var1 + var2
    else:
      ans = var1 - var2
      while ans < 0:
        var1 += 1
        ans = var1 - var2
    equation_set1 = [f"{var1} + {var2} = {ans}", f"{var1} - {var2} = {ans}"]
    return equation_set1[x], ans
  elif (tier==2):
    x = random.randint(0,1)
    ans = -1
    if x == 0:
      ans = var1 + var2 - var3
      while ans < 0:
        var1 += 1
        ans = var1 + var2 - var3
    else:
      ans = var1 - var2 + var3
      while ans < 0:
        var1 += 1
        ans = var1 - var2 + var3
    equation_set2 = [f"({var1} + {var2}) - {var3} = {ans}", f"{var1} - ({var2} + {var3}) = {ans}"]
    chosen_equation = equation_set2[x]
    return chosen_equation, ans
  elif (tier==3):
    x = random.randint(0,1)
    ans = 0
    if x == 0:
      ans = var1 * var2
    else:
      while True:
        ans = var1 / var2
        if var1 % var2 == 0:
          break
        else:
          var1 = random.randint(1,50)
          var2 = random.randint(1,10)
    equation_set3 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = equation_set3[x]
    return chosen_equation, int(ans)
  elif (tier==4):
    x = random.randint(0,1)
    ans = 0
    if x == 0:
      ans = var1 * var2
    else:
      while True:
        ans = var1 / var2
        if var1 % var2 == 0:
          break
        else:
          var1 = random.randint(1,200)
          var2 = random.randint(1,100)
    equation_set4 = [f"{var1} x {var2} = {ans}", f"{var1} / {var2} = {ans}"]
    chosen_equation = equation_set4[x]
    return chosen_equation, int(ans)
  elif (tier==5):
    x = random.randint
    ans = -1
    if x == 0:
      ans = var1 * var2 - var3
      while ans < 0:
        var3 = var3 - 1
        ans = var1 * var2 - var3
    else:
      ans = var1 + var2 - var3 / var4
      while var3 % var4 != 0:
        var3 = random.randint(1,50)
        var4 = random.randint(1,50)
      while ans < 0:
        var1 += 1
        ans = var1 + var2 - var3 / var4
    equation_set5 = [f"({var1} x {var2}) - {var3} = {ans}", f"({var1} + {var2}) - ({var3} / {var4}) = {ans}"]
    chosen_equation = equation_set5[x]
    return chosen_equation, int(ans)
  
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

def fake_answer1(answer):
  f_answer1 = answer + 2
  return f_answer1
def fake_answer2(answer):
  f_answer2 = answer - 2
  return f_answer2