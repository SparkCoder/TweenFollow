import bpy

from bpy.types import Panel, UILayout, Context
from bpy.props import BoolProperty

from ..lists import TWEEN_UL_List

from ....core.common import Registerable, PropertyHolder


class TWEEN_PT_Panel_Main(Panel, Registerable):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Tween Follow'
    bl_category = 'Tween Follow'

    tween_follow_is_playing = PropertyHolder(
        name='tween_follow_is_playing',
        property=BoolProperty(
             name='tween_follow_is_playing',
             default=False
        )
    )

    @classmethod
    def register_cls(cls):
        # Register properties
        setattr(bpy.types.Scene, cls.tween_follow_is_playing.name,
                cls.tween_follow_is_playing.property)
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)
        # Unregister properties
        delattr(bpy.types.Scene, cls.tween_follow_is_playing.name)

    def draw(self, context: Context):
        layout: UILayout = self.layout

        row = layout.row()
        row.label(text='Tweens', icon='GP_SELECT_POINTS')

        row = layout.row(align=True)
        if context.scene.tween_follow_is_playing:
            row.operator('tween_follow.stop_tweens',
                         text='STOP', icon='PAUSE')
        else:
            row.operator('tween_follow.start_tweens',
                         text='START', icon='PLAY')

        # row = layout.row()
        # col = row.column()
        row.operator('tween_follow.add_tween', text='', icon='ADD')
        # col = row.column()
        row.operator('tween_follow.remove_tween', text='', icon='REMOVE')

        row = layout.row()
        TWEEN_UL_List.draw('tween_list', context, row)

        tween_list_items = context.scene.tween_list_items
        tween_list_index = context.scene.tween_list_index
        if len(tween_list_items) > 0 and tween_list_index >= 0:
            tween_list_item = context.scene.tween_list_items[context.scene.tween_list_index]

            layout.separator()

            row = layout.row()
            row.label(text='Tween Source', icon='CURVE_NCIRCLE')

            row = layout.row()
            row.prop_search(tween_list_item, 'tween_source',
                            context.scene, 'objects', text='')

            row = layout.row()
            row.label(text='Tween Target', icon='FORCE_CURVE')

            row = layout.row()
            row.prop(tween_list_item, 'tween_target_type', text='')

            row = layout.row()
            if tween_list_item.tween_target_type == 'Coll':
                row.prop_search(tween_list_item, 'tween_target_coll',
                                bpy.data, 'collections', text='')
            else:
                box = layout.box()
                for i, tween_target_item in enumerate(tween_list_item.tween_target_list):
                    row = box.row()
                    col = row.column()
                    col.prop_search(
                        tween_target_item, 'tween_target', bpy.data, 'objects', text='')
                    col = row.column()
                    col.operator('tween_follow.remove_tween_target',
                                 text='', icon='X').tween_target_index = i

                row = box.row()
                row.operator('tween_follow.add_tween_target',
                             text='ADD', icon='ADD')
