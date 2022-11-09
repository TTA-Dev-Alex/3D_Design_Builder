#lets start by creating a new object to Scale
bpy.ops.mesh.primitive_cube_add()

#now lets create another variable for easy access to our new object
thing = bpy.context.active_object

#now lets scale it! Hint: (X, Y, Z)
thing.scale = (2, 1, 1)

#this will scale it x2 by the X axis!
