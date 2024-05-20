from ursina import Ursina, Entity, EditorCamera, color

app = Ursina()

ground = Entity(model='plane', scale=(128, 1, 128), color=color.green)

editor_camera = EditorCamera()

app.run()
