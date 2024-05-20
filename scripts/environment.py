# scripts/environment.py

from ursina import Entity, color

def create_environment():
    ground = Entity(model='plane', scale=(128, 1, 128), color=color.green)
    return ground
