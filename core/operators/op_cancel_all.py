import bpy

from bpy.types import Operator

from . import Registerable, op_registry


class EF_OT_Cancel_All_Op(Operator, Registerable):
    bl_idname = 'object.cancel_all_mods'
    bl_label = 'Cancel all'
    bl_description = 'Cancel all operators on active object'

    @classmethod
    def register_cls(cls):
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)

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


op_registry += [EF_OT_Cancel_All_Op]
