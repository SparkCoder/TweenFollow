import bpy

from bpy.types import Operator


class EF_OT_Cancel_All_Op(Operator):
    bl_idname = 'object.cancel_all_mods'
    bl_label = 'Cancel all'
    bl_description = 'Cancel all operators on active object'

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == 'OBJECT':
                return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active

        active_obj.modifiers.clear()

        return {'FINISHED'}
