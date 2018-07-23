from player import Player
class Center(Player):
    def run_play(self, play):
        if play in self.playbook:
            print ("Center: " + play)
        else:
            print("Center: I don't know that play...")
