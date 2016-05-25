import bpy

def Draw_Base_Plate():
	bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(0.175,0,0.09))
	bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(-0.175,0,0.09))

	bpy.ops.object.select_pattern(pattern="Cube")
	bpy.ops.object.delete(use_global=False)

	bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(-0.175,0,0.09))
	
#########################################################

# ADDING BASE PLATE
	bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=0.005, location=(0,0,0.09))
	
	#Adding boolean difference modifier from first cube
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube"]
	bpy.ops.object.modifier_apply(modifier="Boolean")
	
	############################################################
	
	#Adding boolean difference modifiers fomr second cube
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube.001"]
	bpy.ops.object.modifier_apply(modifier="Boolean")
	
	############################################################
	
	#Deselecting cylinder and delete cubes
	bpy.ops.object.select_pattern(pattern="Cube")
	bpy.ops.object.select_pattern(pattern="Cube.001")	
	bpy.data.objects['Cylinder'].select = False
	bpy.ops.object.delete(use_global=False)
	
#This function will draw motors and wheels

def Draw_Motors_Wheels():
	#Creating First wheels
	bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.01, location=(0,0,0.07))
	#Rotation
	bpy.context.object.rotation_euler[1] = 1.5708
	#translation
	bpy.context.object.location[0] = 0.135
	
	#Creating Second Wheels
	bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.01, location=(0,0,0.07))
	#Rotation
	bpy.context.object.rotation_euler[1] = 1.5708
	#translation
	bpy.context.object.location[0] = -0.135
	
	#Adding motors
	bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.06, location=(0.075,0,0.075))
	bpy.context.object.rotation_euler[1] = 1.5708
	
	bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.06, location=(-0.075,0,0.075))
	bpy.context.object.rotation_euler[1] = 1.5708
	
	#Adding motor shaft
	bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.04, location=(0.12,0,0.075))
	bpy.context.object.rotation_euler[1] = 1.5708
	
	bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=0.04, location=(-0.12,0,0.075))
	bpy.context.object.rotation_euler[1] = 1.5708
	
	#Adding castor wheel
	
	bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.05, location=(0,0.125,0.065))
	bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.05, location=(0,-0.125,0.065))
	
	#Adding Kinect
	bpy.ops.mesh.primitive_cube_add(radius=0.04, location=(0,0,0.26))
	
#This function will draw Middle Plate
def Draw_Middle_Plate():
	bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=0.005, location=(0,0,0.22))
	
#Adding top plate
def Draw_Top_Plate():
	bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=0.005,location=(0,0,0.37))

#Adding Support tubes
def Draw_Support_Tubes():
	#Cylinder
	bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.30, location=(0.09,0.09,0.23))
	bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.30, location=(-0.09,0.09,0.23))
	bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.30, location=(-0.09,-0.09,0.23))
	bpy.ops.mesh.primitive_cylinder_add(radius=0.007, depth=0.30, location=(0.09,-0.09,0.23))
	
#This function will export to STL
def Save_to_STL():
	bpy.ops.object.select_all(action='SELECT')
	#bpy.ops.mesh.select_all(action='TOGGLE')
	bpy.ops.export_mesh.stl(check_existing=True, filepath="E:/exported.stl", filter_glob="*.stl", ascii=False, use_mesh_modifiers=True, axis_forward="Y",axis_up="Z",global_scale=1.0)
	

#MAIN CODE

if __name__ == "__main__":
	Draw_Base_Plate()
	Draw_Motors_Wheels()
	Draw_Middle_Plate()
	Draw_Top_Plate()
	Draw_Support_Tubes()
	Save_to_STL()
	
	
	
		
