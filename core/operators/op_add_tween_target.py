import bpy

from bpy.types import Operator, Context

from ..common import Registerable


class TWEEN_OT_Add_Tween_Target_Op(Operator, Registerable):
    bl_idname = 'tween_follow.add_tween_target'
    bl_label = 'Add Tween Target'
    bl_description = 'Adds a new tween target object'

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
        tween_list_items = context.scene.tween_list_items
        tween_list_index = context.scene.tween_list_index
        return len(tween_list_items) > 0 and tween_list_index >= 0 and tween_list_index < len(tween_list_items)

    def execute(self, context: Context):
        tween_list_items = context.scene.tween_list_items
        tween_list_index = context.scene.tween_list_index

        tween_list_items[tween_list_index].tween_target_list.add()

        return {'FINISHED'}
