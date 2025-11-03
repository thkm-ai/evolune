import bpy
import random
import bmesh

def generate_tactical_companion():
    # Clear workspace of corporate-issued models
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Create base form optimized for Tibara conditions
    bpy.ops.mesh.primitive_uv_sphere_add(segments =48, ring_
count =24, radius =1.2)
    companion = bpy.context.active_object
    companion.name = "TibaraSurvivor"

    # Add subdivision for detail while maintaining performance
    modifier = companion.modifiers.new(name="DetailLevel",
type='SUBSURF')
    modifier.levels =2
    bpy.ops.object.modifier_apply(modifier="DetailLevel")

    # Apply environmental adaptations based on Tibara analysis
    adaptation_scale = (
        random.uniform (0.9, 1.3), # Width variation for
        # terrain navigation
        random.uniform (0.8, 1.2), # Height variation for acid
        # rain protection
        random.uniform(0.9, 1.4) # Depth variation for
        # stability
    )
    companion.scale = adaptation_scale

    # Create protective material resistant to acid rain
    material = bpy.data.materials.new(name="TibaraResistant")
    companion.data.materials.append(material)
    material.use_nodes = True

    # Set material properties for Tibara survival (darker
    # colors, higher durability)
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (
        random.uniform (0.1, 0.4), # Darker base for heat
        # resistance
        random.uniform (0.1, 0.3), # Reduced green for
        # camouflage
        random.uniform (0.2, 0.5), # Controlled blue for
        # distinction
        1.0
    )
    bsdf.inputs['Roughness'].default_value =0.8 # High
    # roughness for acid resistance
    bsdf.inputs['Metallic'].default_value =0.3 # Some
    # metallic properties for durability
    
    print (f"Generated tactical companion: {companion.name}")
    print(f"Adaptations: Scale {adaptation_scale}")
    return companion

# Generate a squad of survival companions
squad_size =5
for i in range(squad_size):
    companion = generate_tactical_companion()
    print(f"Companion {i+1} ready for deployment")

print("Tactical squad generation complete")