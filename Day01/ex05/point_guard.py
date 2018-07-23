from player import Player
class PointGuard(Player):
    def run_play(self, play):
        if play in self.playbook:
            print("Point Guard: " +  play)
        else:
            print("Point Guard: I don't know that play...")
