#create a variable for easy use
#this variable refers to the current object
thing = bpy.context.active_object

#now lets move the thing UP
thing.location[2] = 3

#[0] is X axis (left & right)
#[1] is Y axis (forward & back)
#[2] is Z axis (up & down)
