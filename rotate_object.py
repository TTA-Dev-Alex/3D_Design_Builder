#import math to calculate rotation
import math
#variable for the selected object
thing = bpy.context.active_object
#the object here is rotated 90 degrees on the X axis
thing.rotation_euler[0] = math.radians(90)
#hint
# [0] = x
# [1] = y
# [2] = z
