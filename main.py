# main.py

from ursina import Ursina, EditorCamera
from scripts.player import Player
from scripts.environment import create_environment

app = Ursina()

player = Player()
ground = create_environment()
editor_camera = EditorCamera()

app.run()
