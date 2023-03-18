import bpy

from bpy.types import Operator, Context

from ..common import Registerable


class TWEEN_OT_Add_Tween_Op(Operator, Registerable):
    bl_idname = 'tween_follow.add_tween'
    bl_label = 'Add Tween'
    bl_description = 'Adda a new tween'
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def register_cls(cls):
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)

    @classmethod
    def poll(cls, context: Context):
        return True

        # obj = context.object

        # if obj is not None:
        #     if obj.mode == 'OBJECT':
        #         return True

        # return False

    def execute(self, context: Context):
        tween_list_items = context.scene.tween_list_items
        tween_list_items.add()

        # context.scene.tween_list_index = len(tween_list_items) - 1

        return {'FINISHED'}
