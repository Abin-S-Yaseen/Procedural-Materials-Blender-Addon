bl_info = {
    "name": "Procedural Materials Addon",
    "author": "Abin S Yaseen",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Toolshelf",
    "description": "A collection of procedural materials",
    "warning": "",
    "wiki_url": "",
    "category": "Add Shader",
}

import bpy


    #Operator for the Gold Shader
class SHADER_OT_GOLD(bpy.types.Operator):
    
    bl_label = "Gold"
    bl_idname = 'shader.gold_operator'
    
    def execute(self, context):
        
            #Create a Shader Material and name it Gold
        material_gold = bpy.data.materials.new(name= "Gold")
        material_gold.use_nodes = True
        
        material_output = material_gold.node_tree.nodes.get('Material Output')
        material_output.location = (600,0)
        material_output.select = False
        
        
            #Create reference to the RGB node      
        rgb_node = material_gold.node_tree.nodes.new('ShaderNodeRGB')
        rgb_node.location = (0,-100)
        rgb_node.outputs[0].default_value = (1, 0.766, 0.336, 1)
        rgb_node.select = False  # deselects it
        rgb_node.hide = True  # for minimizing the node
        
        
            #Create reference to the Principled Node
        principled = material_gold.node_tree.nodes.get('Principled BSDF')
        principled.location = (200,0)
        principled.select = False
        principled.inputs[4].default_value = 1.0
        principled.inputs[6].default_value = 1.0
        principled.inputs[9].default_value = 0.371
        
        
            #for connecting two boxes with a link
        material_gold.node_tree.links.new(rgb_node.outputs[0], principled.inputs[0])
            
            
            #Add Material to the currently selected object
        bpy.context.object.active_material = material_gold
            
        return {'FINISHED'}
    
class SHADER_OT_WOOD(bpy.types.Operator):
    
    bl_label = "Wood"
    bl_idname = 'shader.wood_operator'
    
    def execute(self, context):
        
        material_wood = bpy.data.materials.new(name= "Wood")
        material_wood.use_nodes = True
        
        texture_coordinate = material_wood.node_tree.nodes.new('ShaderNodeTexCoord')
        texture_coordinate.location = (-900,0)
        texture_coordinate.select = False
        
        mapping = material_wood.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-600,0)
        mapping.inputs[3].default_value[0] = 0.45
        mapping.inputs[3].default_value[1] = 2.77
        mapping.select = False
        
        musgrave = material_wood.node_tree.nodes.new('ShaderNodeTexMusgrave')
        musgrave.location = (-300,0)
        musgrave.inputs[2].default_value = 0.64
        musgrave.select = False
        
        noise = material_wood.node_tree.nodes.new('ShaderNodeTexNoise')
        noise.location = (0,0)
        noise.inputs[2].default_value = 2.15
        noise.inputs[3].default_value = 18
        noise.inputs[4].default_value = 0.817
        noise.inputs[5].default_value = 0.750
        noise.select = False
        
        colorramp1 = material_wood.node_tree.nodes.new('ShaderNodeValToRGB')
        colorramp1.location = (300,300)
        colorramp1.color_ramp.elements.new(position=0.377)
        colorramp1.color_ramp.elements[2].position = 0.668
        colorramp1.color_ramp.elements[0].color = (1, 0.25, 0.058, 1) 
        colorramp1.color_ramp.elements[1].color = (0.784, 0.3, 0.091, 1)       
        colorramp1.color_ramp.elements[2].color = (0, 0, 0, 1)
        colorramp1.color_ramp.interpolation = 'EASE'
        colorramp1.select = False
        
        colorramp2 = material_wood.node_tree.nodes.new('ShaderNodeValToRGB')
        colorramp2.location = (300,0)
        colorramp2.color_ramp.elements[0].position = 0.441
        colorramp2.select = False
        
        bump = material_wood.node_tree.nodes.new('ShaderNodeBump')
        bump.location = (300,-300)
        bump.inputs[0].default_value = 0.143
        bump.select = False
        
        principled = material_wood.node_tree.nodes.get('Principled BSDF')
        principled.location = (600,0)
        principled.inputs[1].default_value = 0.041
        principled.select = False
        
        material_output = material_wood.node_tree.nodes.get('Material Output')
        material_output.location = (900,0)
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