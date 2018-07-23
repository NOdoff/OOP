from player import Player
class ShootingGuard(Player):
    def run_play(self, play):
        if play in self.playbook:
            print("Shooting Guard: " +  play)
        else:
            print("Shooting Guard: I don't know that play...")
