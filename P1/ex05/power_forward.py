from player import Player
class PowerForward(Player):
    def run_play(self, play):
        if play in self.playbook:
            print("Power Forward: " +  play)
        else:
            print("Power Forward: I don't know that play...")
