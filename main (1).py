class player:

  def play(self):
    print("the player is playing cricket.")


class Batsman(player):

  def play(self):
    print("The batsman is batting.")


class bowler(player):

  def play(self):
    print("The bowler is bowling")


batsman = Batsman()
Bowler = bowler()

batsman.play()
Bowler.play()
