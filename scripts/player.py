# scripts/player.py

from ursina import Entity, Vec3, time, held_keys, camera, mouse, color

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.position = Vec3(0, 1, 0)
        self.speed = 5
        self.rotation_speed = 100

        # Hide the mouse cursor and lock it in the window
        mouse.locked = True

        # Attach camera to player
        camera.parent = self
        camera.position = (0, 1.8, 0)  # Position camera at player's eye level
        camera.rotation = (0, 0, 0)    # Initial camera rotation
        self.mouse_sensitivity = Vec3(40, 40, 40)

    def update(self):
        self.move()
        self.rotate()

    def move(self):
        speed = self.speed * time.dt
        if held_keys['w']:
            self.position += self.forward * speed
        if held_keys['s']:
            self.position -= self.forward * speed
        if held_keys['a']:
            self.position -= self.right * speed
        if held_keys['d']:
            self.position += self.right * speed

    def rotate(self):
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1] * time.dt
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0] * time.dt
        camera.rotation_x = max(min(camera.rotation_x, 90), -90)  # Limit vertical rotation to avoid flipping
