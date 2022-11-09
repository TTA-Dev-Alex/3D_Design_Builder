#add the bottom sphere
bpy.ops.mesh.primitive_uv_sphere_add()

#add the middle sphere, move it up and scale it down
bpy.ops.mesh.primitive_uv_sphere_add()
thing = bpy.context.active_object
thing.location[2] = 1.5
thing.scale = (0.75, 0.75, 0.75)

#add the top sphere, move it up more, and scale it down more
bpy.ops.mesh.primitive_uv_sphere_add()
thing = bpy.context.active_object
thing.location[2] = 2.5
thing.scale = (0.5, 0.5, 0.5)
