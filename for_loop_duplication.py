import bpy
import random

spacing = 2.2
for x in range(10):
    for y in range(10):
        bpy.ops.object.duplicate(linked=False)
        location = (x * spacing, y * spacing, random.random() * 2)
        thing = bpy.context.active_object
        thing.location = location
