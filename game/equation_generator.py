'''Takes problem tier from the game, picks an appropriate equation,
assigns variable values, returns equations and solutions to generated problem'''
import random

def main():
  tier = 1 #variable pulled from game based off score, affects problem difficulty
  var1,var2,var3,var4 = variable_maker(tier) #random variables are created based on the tier
  equation, anwser= (format_picker(tier,var1,var2,var3,var4)) #the variable are then used to make an equation and the anwser is calculated.
  return equation, anwser

def format_picker (tier,var1,var2,var3,var4):
  #teir 1 and it's formats
  if (tier==1):
    #pick a random equation format.
    x = random.randint(0,1)
    if x == 0:
      ans = var1 + var2
    else:
      ans = var1 - var2
      while ans < 0:
        # if the anwser is less then zero. Then Var1 is added on to until it is equal to zero
        var1 += 1
        ans = var1 - var2
    #The equation is saved as a string based on the format chosen by the code
    equation_set1 = [f"{var1} + {var2} =", f"{var1} - {var2} ="]
    return equation_set1[x], ans
  elif (tier==2):
    #tier two and it's formats
    x = random.randint(0,1)
    ans = -1
    if x == 0:
      ans = var1 + var2 - var3
      while ans < 0:
        #if var1 + var2 is less then var3. Var1 is added onto until the anwser is zero
        var1 += 1
        ans = var1 + var2 - var3
    else:
      ans = var1 - var2 + var3
      while ans < 0:
        var1 += 1
        ans = var1 - var2 + var3
    #equations are turned into strings and the anwser is returned separately
    equation_set2 = [f"({var1} + {var2}) - {var3} =", f"{var1} - ({var2} + {var3}) ="]
    chosen_equation = equation_set2[x]
    return chosen_equation, ans
  elif (tier==3):
    #tier three equations and formats
    x = random.randint(0,1)
    ans = 0
    if x == 0:
      ans = var1 * var2
    else:
      while True:
        ans = var1 / var2
        if var1 % var2 == 0:
          #check to make sure there is no remainder after var1 is divided by var2
          break
        else:
          #The numbers are selected at random again. Still looking for two numbers that divide evenly into eachother.
          var1 = random.randint(1,50)
          var2 = random.randint(1,10)
    #the chosen format is saved as a string.
    equation_set3 = [f"{var1} x {var2} =", f"{var1} / {var2} ="]
    chosen_equation = equation_set3[x]
    return chosen_equation, int(ans)
  elif (tier==4):
    #tier four
    x = random.randint(0,1)
    ans = 0
    if x == 0:
      ans = var1 * var2
    else:
      while True:
        ans = var1 / var2
        if var1 % var2 == 0:
          #make sure that var1 can be evenly divided by var2
          break
        else:
          #otherwise, pick two random numbers and try again until the two evenly divide
          var1 = random.randint(1,200)
          var2 = random.randint(1,100)
    #equations are saved as a string and the anwser carries an int
    equation_set4 = [f"{var1} x {var2} =", f"{var1} / {var2} ="]
    chosen_equation = equation_set4[x]
    return chosen_equation, int(ans)
  elif (tier==5):
    #tier 5
    x = random.randint
    ans = -1
    if x == 0:
      ans = var1 * var2 - var3
      while ans < 0:
        #if the anser is negative. Remove 1 from var 3 until the ans is no longer negative.
        var3 = var3 - 1
        ans = var1 * var2 - var3
    else:
      ans = var1 + var2 - var3 / var4
      while var3 % var4 != 0:
        #if var3 and var4 do not divide evenly. Var3 and var4 are randomized agian until they divide evenly.
        var3 = random.randint(1,50)
        var4 = random.randint(1,50)
      while ans < 0:
        var1 += 1
        ans = var1 + var2 - var3 / var4
    #the equation is saved as a string while the anwser is saved separetly as an int
    equation_set5 = [f"({var1} x {var2}) - {var3} =", f"({var1} + {var2}) - ({var3} / {var4}) ="]
    chosen_equation = equation_set5[x]
    return chosen_equation, int(ans)
  
def variable_maker(tier):
    #variables start at zero and all relevent variable should be changed by the end of this function.
    var1 = 0 
    var2 = 0
    var3 = 0
    var4 = 0
    if tier == 1:
      #tier1 we only need var 1 and var2
      var2 = 1
      #1-10
      while var1 < var2:
        var1 = random.randint(0,10)
        var2 = random.randint(0,10)
        var3 = 0
        var4 = 0
      return var1,var2,var3,var4
    elif tier == 2:
      #var 2 we need vars 1, 2, and 3
      var3 = 1
      #10-100e
      while var3 < var2 + var1:
        var1 = random.randint(0,100)
        var2 = random.randint(0,100)
        var3 = random.randint(0,100)
        var4 = 0
      return var1,var2,var3,var4
    elif tier == 3:
      #tier 3 needs 1 and 2
      #1-10
      var1 = random.randint(1,10)
      var2 = random.randint(1,10)
      var3 = 0
      var4 = 0
      return var1,var2,var3,var4
    elif tier == 4:
      #1-50
      #tier 4 needs 1 and 2 
      var1 = random.randint(1,50)
      var2 = random.randint(1,50)
      var3 = 0
      var4 = 0
      return var1,var2,var3,var4
    elif tier == 5:
      #1-100 all whole numbers.
      #tier 5 needs all four variables to be generated.
      var1 = random.randint(1,100)
      var2 = random.randint(1,100)
      var3 = random.randint(1,100)
      var4 = random.randint(1,100)
      return var1,var2,var3,var4
    else:
      print("wot")

def fake_answer1(answer):
  # the first fake anwser is generated from the real one.
  negative = random.choice([True, False])

  add =  random.randint(1,10)

  if negative:
    #if negative is True, then the number is made negative. 
    add *= -1
  f_answer1 = answer + add
  return f_answer1
def fake_answer2(answer, prev=False):
  #this fake anwser is generated so that it dosn't match the first one or the anwser
  if prev == False:
    return fake_answer1(answer)
  else:
    f_answer = fake_answer1(answer)
    while f_answer == prev:
      f_answer = fake_answer1(answer)

    return f_answer

   