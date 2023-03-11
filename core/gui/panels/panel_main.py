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
        col.operator('tween_list_items.add_tween', text='Add Tween')
        col = row.column()
        col.operator('tween_list_items.remove_tween', text='Remove Tween')

        row = layout.row()
        TWEEN_UL_List.draw('tween_list', context, row)

        tween_list_items = context.scene.tween_list_items
        tween_list_index = context.scene.tween_list_index
        if len(tween_list_items) > 0 and tween_list_index >= 0:
            row = layout.row()
            row.prop_search(context.scene.tween_list_items[context.scene.tween_list_index], 'tween_source',
                            context.scene, 'objects')
