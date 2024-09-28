# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Lock Camera and/or Cursor",
    "author": "Blender Bob / ChatGPT",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Header",
    "description": "Toggle lock camera and/or cursor",
    "category": "Object"
    "support": "COMMUNITY"      
}

import bpy

class OBJECT_OT_toggle_lock_camera(bpy.types.Operator):
    bl_idname = "object.toggle_lock_camera"
    bl_label = ""

    def execute(self, context):
        view3d = context.space_data
        view3d.lock_camera = not view3d.lock_camera
        return {'FINISHED'}

class OBJECT_OT_toggle_lock_cursor(bpy.types.Operator):
    bl_idname = "object.toggle_lock_cursor"
    bl_label = ""

    def execute(self, context):
        view3d = context.space_data
        view3d.lock_cursor = not view3d.lock_cursor
        return {'FINISHED'}

def toggle_lock_camera_button(self, context):
    if context.space_data.lock_camera:
        icon = 'OUTLINER_OB_CAMERA'
    else:
        icon = 'CAMERA_DATA'
    self.layout.operator(OBJECT_OT_toggle_lock_camera.bl_idname, icon=icon)

def toggle_lock_cursor_button(self, context):
    if context.space_data.lock_cursor:
        icon = 'PIVOT_CURSOR'
    else:
        icon = 'CURSOR'
    self.layout.operator(OBJECT_OT_toggle_lock_cursor.bl_idname, icon=icon)

def register():
    bpy.utils.register_class(OBJECT_OT_toggle_lock_camera)
    bpy.utils.register_class(OBJECT_OT_toggle_lock_cursor)
    bpy.types.VIEW3D_HT_header.append(toggle_lock_camera_button)
    bpy.types.VIEW3D_HT_header.append(toggle_lock_cursor_button)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_toggle_lock_camera)
    bpy.utils.unregister_class(OBJECT_OT_toggle_lock_cursor)
    bpy.types.VIEW3D_HT_header.remove(toggle_lock_camera_button)
    bpy.types.VIEW3D_HT_header.remove(toggle_lock_cursor_button)

if __name__ == "__main__":
    register()
