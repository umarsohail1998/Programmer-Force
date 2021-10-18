# Q2
import random

class Game:
  dice = [1,2,3,4,5,6]
  coin = ['Head', 'Tail']

  def __init__(self, P1_Name, P2_Name):
    self.P1_N, self.P1_s = P1_Name, 0
    self.P2_N, self.P2_s = P2_Name, 0
    
  def rolldice(self):
    print("-- Dice Rolling --")
    
    tmp = random.choice(self.dice)
    self.P1_s += tmp if tmp%2==0 else (tmp*2)

    tmp = random.choice(self.dice)
    self.P2_s += tmp if tmp%2==0 else (tmp*2)
    print(f"Player: {self.P1_N}, Score: {self.P1_s}")
    print(f"Player: {self.P2_N}, Score: {self.P2_s}")

  def toss_coin(self):
    print("-- Coin Tossing --")
    tmp = random.choice(self.coin)
    self.P1_s += (2*self.P1_s) if tmp=='head' else (self.P1_s/2)

    tmp = random.choice(self.coin)
    self.P2_s += (2*self.P2_s) if tmp=='head' else (self.P2_s/2)
    print(f"Player: {self.P1_N}, Score: {self.P1_s}")
    print(f"Player: {self.P2_N}, Score: {self.P2_s}")
    
  def start(self):
      print(f"Game Start Btw: {self.P1_N}, {self.P2_N}")
      self.rolldice()
      self.toss_coin()
      if self.P1_s > self.P2_s:
        print(f'\nWinner: {self.P1_N}, Score: {self.P1_s}')
        return self.P1_N, self.P1_s
      else:
        print(f'\nWinner: {self.P2_N}, Score: {self.P1_s}')
        return self.P2_N,self.P2_s
        
        
if __name__ == "__main__": 
	print("Game1")
	win1, s = Game('P1','P2').start()
	print("\n")
	print("Game2")
	win2, s = Game('P3','P4').start()
	print("\n")
	print("Game3")
	win, s = Game(win1,win2).start()
	print("\n")
