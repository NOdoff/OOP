#!/usr/bin/env python3

from player import Player
from point_guard import PointGuard
from center import Center
from small_forward import SmallForward
from shooting_guard import ShootingGuard
from power_forward import PowerForward

def main():

    pg = PointGuard()
    c = Center()
    sf = SmallForward()
    sg = ShootingGuard()
    pf = PowerForward()
    pg.run_play("I'll dribble penetrate")
    c.run_play("I'll cut to the corner")
    sf.run_play("I'll set the first pick")
    sg.run_play("I'll run to the wing")
    pf.run_play("I'll set the second pick")
    pg.run_play("I'll dribble past the screens to the post")
    c.run_play("I'll cut to the top of the key")
    sf.run_play("I'll set the first pick and roll to the basket")
    sg.run_play("I'll maneuver to the low block and set a screen")
    pf.run_play("I'll set the second pick and screen the shooting guard")


if __name__ == "__main__":
    main()
