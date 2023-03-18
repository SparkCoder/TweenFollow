import bpy

from bpy.types import Operator, Context
from bpy.props import IntProperty

from ..common import Registerable, PropertyHolder


class TWEEN_OT_Remove_Tween_Target_Op(Operator, Registerable):
    bl_idname = 'tween_follow.remove_tween_target'
    bl_label = 'Remove Tween Target'
    bl_description = 'Removes a tween target'
    bl_options = {"REGISTER", "UNDO"}

    tween_target_index: IntProperty(
        name='tween_target_index',
        default=0,
    )

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
        tween_target_list = tween_list_items[tween_list_index].tween_target_list

        if len(tween_target_list) > 0 and self.tween_target_index >= 0 and self.tween_target_index < len(tween_target_list):
            tween_target_list.remove(self.tween_target_index)

        return {'FINISHED'}
