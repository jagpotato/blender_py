import bpy
import math
import sys
sys.path.append('.')
import env

ROT_QUATER = math.pi / 2

def delete_all():
  for item in bpy.context.scene.objects:
    bpy.context.scene.objects.unlink(item)

  for item in bpy.data.objects:
    bpy.data.objects.remove(item)

  for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

  for item in bpy.data.materials:
    bpy.data.materials.remove(item)

def add_cone():
  bpy.ops.mesh.primitive_cone_add(
    vertices = 6,
    radius1 = 6,
    radius2 = 3,
    location = (3, 0, 0),
    rotation = (0.5, 0, 0)
  )

def add_text(text) :
  bpy.ops.object.text_add()
  ob = bpy.context.object
  ob.data.body = text
  ob.data.extrude = 0.1
  ob.rotation_euler[0] = ROT_QUATER
  ob.rotation_euler[2] = ROT_QUATER
  ob.data.align_x = 'CENTER'
  ob.data.align_y = 'CENTER'

  bpy.data.fonts.load(env.FONT_PATH)
  ob.data.font = bpy.data.fonts.get('Meiryo')
  # print(bpy.data.fonts[1])

def export_object(path = env.OUTPUT_PATH):
  bpy.ops.export_scene.fbx(
    filepath = path,
    version = 'BIN7400',
    ui_tab = 'GEOMETRY',
    use_mesh_modifiers = True,
    use_mesh_modifiers_render = True,
    mesh_smooth_type = 'OFF'
  )

if __name__ == "__main__":
  delete_all()
  # add_cone()
  add_text('漢字')
  # export_object()