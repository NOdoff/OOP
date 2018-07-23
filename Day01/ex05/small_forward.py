from player import Player
class SmallForward(Player):
    def run_play(self, play):
        if play in self.playbook:
            print ("Small Forward: " + play)
        else:
            print("Small Forward: I don't know that play...")
