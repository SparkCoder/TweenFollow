import bpy

from bpy.types import Operator

from ..common import Registerable


class TWEEN_OT_Remove_Tween_Op(Operator, Registerable):
    bl_idname = 'tween_list_items.remove_tween'
    bl_label = 'Remove Tween'
    bl_description = 'Remove new tween'

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
        return True

        # obj = context.object

        # if obj is not None:
        #     if obj.mode == 'OBJECT':
        #         return True

        # return False

    def execute(self, context):
        tween_list_items = context.scene.tween_list_items
        index = context.scene.tween_list_index

        tween_list_items.remove(index)
        context.scene.tween_list_index = min(
            max(0, index - 1), len(tween_list_items) - 1)

        return {'FINISHED'}
