x = 10
while x < 20:
	bpy.ops.object.duplicate(linked=False)
	thing = bpy.context.active_object
	thing.location[0] = thing.location[0] + 3
	x = x + 1
