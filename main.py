bl_info = {
    "name": "Procedural Materials Addon",
    "author": "Abin S Yaseen",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Toolshelf",
    "description": "A collection of procedural materials",
    "warning": "",
    "wiki_url": "",
    "category": "Add Shader",
}

import bpy


#shader nodes
principled_node = 'ShaderNodeBsdfPrincipled'
material_output_node = 'ShaderNodeOutputMaterial'
rgb_node = 'ShaderNodeRGB'
texture_coordinate_node = 'ShaderNodeTexCoord'
mapping_node = 'ShaderNodeMapping'
musgrave_node = 'ShaderNodeTexMusgrave'
noise_node = 'ShaderNodeTexNoise'
colorramp_node = 'ShaderNodeValToRGB'
bump_node = 'ShaderNodeBump'
mix_rgb_node = 'ShaderNodeMix'


# Gold material
class SHADER_OT_GOLD(bpy.types.Operator):
    
    bl_label = "Gold"
    bl_idname = 'shader.gold_operator'
    
    
    def execute(self, context):
        
        #Create a Shader Material and name it Gold
        material_gold = bpy.data.materials.new(name= "Gold")
        material_gold.use_nodes = True
        
        node = material_gold.node_tree.nodes
        node.clear()

        material_output = node.new(material_output_node)
        material_output.location = (600,0)
        material_output.select = False
        
        
        #Create reference to the Principled Node
        principled = node.new(principled_node)
        principled.location = (200,0)
        principled.select = False
        principled.inputs[4].default_value = 1.0
        principled.inputs[6].default_value = 1.0
        principled.inputs[9].default_value = 0.27

        texture_coordinate = node.new(texture_coordinate_node)
        texture_coordinate.location = (-700,0)
        texture_coordinate.select = False
        
        mapping = node.new(mapping_node)
        mapping.location = (-500,0)
        mapping.select = False

        musgrave = node.new(musgrave_node)
        musgrave.location = (-300,0)
        musgrave.inputs[2].default_value = 400
        musgrave.inputs[3].default_value = 16
        musgrave.inputs[4].default_value = 0
        musgrave.select = False

        colorramp = node.new(colorramp_node)
        colorramp.location = (-100,0)
        colorramp.color_ramp.elements[0].color = (0.610, 0.337, 0.084, 1)
        colorramp.color_ramp.elements[1].color = (0.279, 0.098, 0.025, 1)
        colorramp.select = False

        noise = node.new(noise_node)
        noise.location = (-300,-300)
        noise.inputs[2].default_value = 12
        noise.inputs[3].default_value = 16
        noise.inputs[4].default_value = 0.45
        noise.inputs[5].default_value = 0
        noise.select = False
        
        bump = node.new(bump_node)
        bump.location = (-100,-300)
        bump.inputs[0].default_value = 0.008
        bump.select = False
        
        #links
        link = material_gold.node_tree.links
        link.new(texture_coordinate.outputs[3], mapping.inputs[0])
        link.new(mapping.outputs[0], musgrave.inputs[0])
        link.new(mapping.outputs[0], noise.inputs[0])
        link.new(musgrave.outputs[0], colorramp.inputs[0])
        link.new(noise.outputs[0], bump.inputs[2])
        link.new(colorramp.outputs[0], principled.inputs[0])
        link.new(bump.outputs[0], principled.inputs[22])
        link.new(principled.outputs[0], material_output.inputs[0])
            
            
        #Add Material to the currently selected object
        bpy.context.object.active_material = material_gold
            
        return {'FINISHED'}

# Metal material
class SHADER_OT_METAL(bpy.types.Operator):
    
    bl_label = "Metal"
    bl_idname = 'shader.metal_operator'
    
    
    def execute(self, context):
        
        #Create a Shader Material and name it Metal
        material_metal = bpy.data.materials.new(name= "Metal")
        material_metal.use_nodes = True
        
        node = material_metal.node_tree.nodes
        node.clear()

        material_output = node.new(material_output_node)
        material_output.location = (600,0)
        material_output.select = False
        
        
        #Create reference to the Principled Node
        principled = node.new(principled_node)
        principled.location = (200,0)
        principled.inputs[6].default_value = 1
        principled.select = False

        texture_coordinate = node.new(texture_coordinate_node)
        texture_coordinate.location = (-1000,0)
        texture_coordinate.select = False
        
        musgrave = node.new(musgrave_node)
        musgrave.location = (-800,-300)
        musgrave.inputs[2].default_value = 1
        musgrave.inputs[3].default_value = 15
        musgrave.inputs[4].default_value = 0
        musgrave.select = False

        mix_rgb = node.new(mix_rgb_node)
        mix_rgb.location = (-300,0)
        mix_rgb.data_type = 'RGBA'
        mix_rgb.blend_type = 'DARKEN'
        mix_rgb.clamp_factor = False
        mix_rgb.inputs[0].default_value = 1
        mix_rgb.select = False

        colorramp = node.new(colorramp_node)
        colorramp.location = (-600,0)
        colorramp.color_ramp.elements[0].position = 0.371
        colorramp.select = False

        colorramp1 = node.new(colorramp_node)
        colorramp1.location = (-100,0)
        colorramp1.color_ramp.elements[0].color = (0.319, 0.319, 0.319, 1)
        colorramp1.select = False

        colorramp2 = node.new(colorramp_node)
        colorramp2.location = (-100,-250)
        colorramp2.color_ramp.elements[0].color = (0.381, 0.381, 0.381, 1)
        colorramp2.color_ramp.elements[1].color = (0.107, 0.107, 0.107, 1)
        colorramp2.select = False

        noise = node.new(noise_node)
        noise.location = (-800,0)
        noise.inputs[2].default_value = 4
        noise.inputs[3].default_value = 15
        noise.inputs[4].default_value = 0.7
        noise.inputs[5].default_value = 0
        noise.select = False
        
        bump = node.new(bump_node)
        bump.location = (0,-500)
        bump.inputs[0].default_value = 0.1
        bump.select = False
        
        #links
        link = material_metal.node_tree.links
        link.new(texture_coordinate.outputs[3],noise.inputs[0])
        link.new(texture_coordinate.outputs[3],musgrave.inputs[0])
        link.new(noise.outputs[0],colorramp.inputs[0])
        link.new(colorramp.outputs[0], mix_rgb.inputs[6])
        link.new(musgrave.outputs[0], mix_rgb.inputs[7])
        link.new(mix_rgb.outputs[2], colorramp1.inputs[0])
        link.new(mix_rgb.outputs[2], colorramp2.inputs[0])
        link.new(mix_rgb.outputs[2], bump.inputs[2])
        link.new(colorramp1.outputs[0], principled.inputs[0])
        link.new(colorramp2.outputs[0], principled.inputs[9])
        link.new(bump.outputs[0], principled.inputs[22])
        link.new(principled.outputs[0], material_output.inputs[0])
            
            
        #Add Material to the currently selected object
        bpy.context.object.active_material = material_metal
            
        return {'FINISHED'}
# wood material
class SHADER_OT_WOOD(bpy.types.Operator):
    
    bl_label = "Wood"
    bl_idname = 'shader.wood_operator'
    
    def execute(self, context):
        
        material_wood = bpy.data.materials.new(name= "Wood")
        material_wood.use_nodes = True
        
        node = material_wood.node_tree.nodes
        node.clear()

        texture_coordinate = node.new(texture_coordinate_node)
        texture_coordinate.location = (-600,0)
        texture_coordinate.select = False
        
        mapping = node.new(mapping_node)
        mapping.location = (-400,0)
        mapping.inputs[3].default_value[0] = 0.45
        mapping.inputs[3].default_value[1] = 2.77
        mapping.select = False
        
        musgrave = node.new(musgrave_node)
        musgrave.location = (-200,0)
        musgrave.inputs[2].default_value = 0.64
        musgrave.select = False
        
        noise = node.new(noise_node)
        noise.location = (0,0)
        noise.inputs[2].default_value = 2.15
        noise.inputs[3].default_value = 18
        noise.inputs[4].default_value = 0.817
        noise.inputs[5].default_value = 0.750
        noise.select = False
        
        colorramp1 = node.new(colorramp_node)
        colorramp1.location = (250,300)
        colorramp1.color_ramp.elements.new(position=0.377)
        colorramp1.color_ramp.elements[2].position = 0.668
        colorramp1.color_ramp.elements[0].color = (1, 0.25, 0.058, 1) 
        colorramp1.color_ramp.elements[1].color = (0.784, 0.3, 0.091, 1)       
        colorramp1.color_ramp.elements[2].color = (0, 0, 0, 1)
        colorramp1.color_ramp.interpolation = 'EASE'
        colorramp1.select = False
        
        colorramp2 = node.new(colorramp_node)
        colorramp2.location = (250,0)
        colorramp2.color_ramp.elements[0].position = 0.441
        colorramp2.select = False
        
        bump = node.new(bump_node)
        bump.location = (250,-300)
        bump.inputs[0].default_value = 0.143
        bump.select = False
        
        principled = node.new(principled_node)
        principled.location = (600,0)
        principled.inputs[1].default_value = 0.041
        principled.select = False
        
        material_output = node.new(material_output_node)
        material_output.location = (1000,0)
        material_output.select = False
        
        
        # links
        link = material_wood.node_tree.links
        link.new(texture_coordinate.outputs[3], mapping.inputs[0])
        link.new(mapping.outputs[0], musgrave.inputs[0])
        link.new(musgrave.outputs[0], noise.inputs[0])
        link.new(noise.outputs[0], colorramp1.inputs[0])
        link.new(noise.outputs[0], colorramp2.inputs[0])
        link.new(noise.outputs[0], bump.inputs[2])
        link.new(colorramp1.outputs[0], principled.inputs[0])
        link.new(colorramp1.outputs[0], principled.inputs[3])
        link.new(colorramp2.outputs[0], principled.inputs[9])
        link.new(bump.outputs[0], principled.inputs[22])
        link.new(principled.outputs[0], material_output.inputs[0])
        
                
        bpy.context.object.active_material = material_wood
        
        return {'FINISHED'}
        
#creat Main Panel
class MainPanel(bpy.types.Panel):
    bl_label = "Procedural Textures"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Addon'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Select a Shader.")
        row = layout.row()
        row.operator('shader.gold_operator')
        row = layout.row()
        row.operator('shader.wood_operator')
        

#registering classes
def register():
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(SHADER_OT_GOLD)
    bpy.utils.register_class(SHADER_OT_WOOD)
    
#unregistering classes
def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(SHADER_OT_GOLD)
    bpy.utils.unregister_class(SHADER_OT_WOOD)

    
if __name__ == "__main__":
    register()  