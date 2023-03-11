import bpy

from bpy.types import Operator

from ...core.common import Registerable


class EF_OT_Apply_All_Op(Operator, Registerable):
    bl_idname = 'object.apply_all_mods'
    bl_label = 'Apply all'
    bl_description = 'Apply all operators on active object'

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

        for mod in active_obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=mod.name)

        return {'FINISHED'}
