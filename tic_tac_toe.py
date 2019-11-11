def tic_tac_toe():
  list = [1,2,3,4,5,6,7,8,9]
  last = 0
  win_chances = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
  def board():
    print("_ _ _")
    
  def chooseplace():
    a = int(input())
    a = a - 1
    if a in range(0,9):
      return a
    else:
      print("this number does not exists on the game board")
  def player1():
    n = chooseplace()
    if list[n] == "X" or list[n] == "O":
      print("you cannot go there")
      player1()
    else:
      list[n] = "X"
  def player2():
    n = chooseplace()
    if list[n] == "X" or list[n] == "O":
      print("this number does not exists on the game board")
    else:
      list[n] = "O"
  def check():
    
    for a in win_chances: 
      count = 0
      if list[a[0]] == list[a[1]] == list[a[2]] == "X":
        print("Player 1 Wins!")
        return True

      if list[a[0]] == list[a[1]] == list[a[2]] == "O":
        print("Player 2 Wins!")
        return True
    for a in range(9):
      if list[a] == "X" or list[a] == "O":
        count += 1
      if count == 9:
        print("The game ends in a Tie\n")
        return True
  while not last:
    board()
    last = check()
    if last == True:
      break
    print("player1 where to keep X")
    player1()
    print()
    board()
    if last == True:
      break
    print("player2 where to keep O")
    player2()
    print()
  if input("play again!:") == "yes":
    print()
    tic_tac_toe()
tic_tac_toe()     
