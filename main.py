# main.py

from ursina import Ursina, Entity, camera, color
from scripts.player import Player
from scripts.environment import create_environment

app = Ursina()

ground = create_environment()

player = Player()

crosshair = Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=(0.02, 0.02),
    position=(0, 0)
)

app.run()
