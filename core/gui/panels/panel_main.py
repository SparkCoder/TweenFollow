import bpy

from bpy.types import Panel, UILayout

from ..lists import TWEEN_UL_List

from ....core.common import Registerable


class TWEEN_PT_Panel_Main(Panel, Registerable):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ease Follow'
    bl_category = 'Ease Follow'

    @classmethod
    def register_cls(cls):
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)

    def draw(self, context):
        layout: UILayout = self.layout

        row = layout.row()

        col = row.column()
        col.operator('object.apply_all_mods', text='App1y all')

        col = row.column()
        col.operator('object.cancel_all_mods', text='Cancel all')

        row = layout.row()
        TWEEN_UL_List.draw('tween_list', context, row)
