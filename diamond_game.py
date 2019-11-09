import random
def random_select_strategy():
  l = [1,2,3,4,5,6]
  return random.choice(l)
def diamond_game():
    c = random_select_strategy()  
    b = True
    userpoints = 0
    systempoints = 0
    while b :
      m = diamond_input_random()
      if m == -1:
        b = False
      else:
        print("Present diamond number is:")
        print(m)
        print("Enter bid for the diamond:")
        x = (input())
        if c == 1:
             b = strategy_random()
             getpoints(m,x,b)
        elif c == 2:
             b = strategy_equal(m)
             getpoints(m,x,b)
        elif c == 3:
             b = strategy_even_odd(m)
             getpoints(m,x,b)
        elif c == 4:
             b = strategy_eveneven_oddodd(m)
             getpoints(m,x,b)
        elif c == 5:
             print("enter increment factor to get incresed:")
             d = int(input())
             b = strategy_increment(m,d)
             getpoints(m,x,b)
        elif c == 6:
             print("enter decrement factor to get incresed:")
             d = int(input())
             b = strategy_decrement(m,d)
             getpoints(m,x,b)
    getresults()    
print(diamond_game())          
def strategy_equal(a):
  print("enter computer input:")
  return a
def strategy_even_odd(a):
  print("enter computer input:")
  if(int(a) % 2 == 0):
    o=['3','5','7','9','J','K']
    return random.choice(o)
  elif(int(a) % 2 != 0):
    e=['2','4','6','8','T','Q','A']
    return random.choice(e)
def strategy_eveneven_oddodd(a):
  print("enter computer input:")
  if(int(a) % 2 == 0):
      e=['2','4','6','8','T','Q','A']
      return random.choice(e)
  elif(int(a) % 2 != 0):
      o=['3','5','7','9','J','K']
      return random.choice(o)
def strategy_increment(n, increment):
    print("enter computer input")
    l = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    if n in l:
        diamond_no_index = l.index(n)
        return(l[diamond_no_index + increment])

def strategy_decrement(n, decrement):
    print("enter computer input")
    l =  [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    if n in l:
        diamond_no_index = 13 + l.index(n)
        return(l[diamond_no_index - decrement])

diamonds=['3','5','7','9','J','K','2','4','6','8','T','Q','A']
def diamondinput_random():
  if len(diamonds) == 0:
    return -1
  randomchoice=random.choice(diamonds)
  decofcards.remove(randomchoice)
  return randomchoice

decofcards=['3','5','7','9','J','K','2','4','6','8','T','Q','A']
def strategy_random():
    randomchoice = random.choice(decofcards)
    decofcards.remove(randomchoice)
    return randomchoice
