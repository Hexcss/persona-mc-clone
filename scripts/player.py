# scripts/player.py

from ursina import Entity, color, Vec3, time, held_keys

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.orange
        self.scale_y = 2
        self.position = Vec3(0, 1, 0)

    def update(self):
        speed = 5 * time.dt
        if held_keys['a']:
            self.x -= speed
        if held_keys['d']:
            self.x += speed
        if held_keys['w']:
            self.z += speed
        if held_keys['s']:
            self.z -= speed
