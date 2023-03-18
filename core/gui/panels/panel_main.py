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
    tween_reset_done = PropertyHolder(
        name='tween_reset_done',
        property=BoolProperty(
             name='tween_reset_done',
             default=True
        )
    )

    @classmethod
    def register_cls(cls):
        # Register properties
        setattr(bpy.types.Scene, cls.tween_follow_is_playing.name,
                cls.tween_follow_is_playing.property)
        setattr(bpy.types.Scene, cls.tween_reset_done.name,
                cls.tween_reset_done.property)
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)
        # Unregister properties
        delattr(bpy.types.Scene, cls.tween_reset_done.name)
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
        row.operator('tween_follow.add_tween', text='', icon='ADD')
        row.operator('tween_follow.remove_tween', text='', icon='REMOVE')
        row.operator('tween_follow.reset_tweens', text='', icon='RECOVER_LAST')

        row = layout.row()
        TWEEN_UL_List.draw('tween_list', context, row)

        tween_list_items = context.scene.tween_list_items
        tween_list_index = context.scene.tween_list_index
        if len(tween_list_items) > 0 and tween_list_index >= 0:
            tween_list_item = context.scene.tween_list_items[context.scene.tween_list_index]

            layout.separator()

            row = layout.row()
            row.label(text='Tween Attractor', icon='CURVE_NCIRCLE')

            row = layout.row()
            row.prop_search(tween_list_item, 'tween_attractor',
                            context.scene, 'objects', text='')

            row = layout.row()
            row.label(text='Tween Target', icon='FORCE_CURVE')

            row = layout.row()
            row.prop(tween_list_item, 'keep_offset',
                     text='Keep Relative Offset')

            row = layout.row()
            row.prop(tween_list_item, 'tween_target_type', text='')

            if tween_list_item.tween_target_type == 'Coll':
                row = layout.row(align=True)
                col = row.column()
                col.prop(tween_list_item.tween_target_coll, 'expanded', text='', icon=(
                    'DOWNARROW_HLT' if tween_list_item.tween_target_coll.expanded else 'RIGHTARROW'), icon_only=True, emboss=False)
                col = row.column()
                col.prop_search(tween_list_item.tween_target_coll, 'tween_target',
                                bpy.data, 'collections', text='')
                if tween_list_item.tween_target_coll.expanded:
                    tween_target_item = tween_list_item.tween_target_coll
                    row_exp = col.row()
                    row_exp.prop(tween_target_item, 'step_per_frame')
            else:
                box = layout.box()
                for i, tween_target_item in enumerate(tween_list_item.tween_target_list):
                    row = box.row(align=True)
                    col = row.column()
                    col.prop(tween_target_item, 'expanded', text='', icon=(
                        'DOWNARROW_HLT' if tween_target_item.expanded else 'RIGHTARROW'), icon_only=True, emboss=False)
                    col = row.column()
                    col.prop_search(
                        tween_target_item, 'tween_target', bpy.data, 'objects', text='')
                    if tween_target_item.expanded:
                        row_exp = col.row()
                        row_exp.prop(tween_target_item, 'step_per_frame')
                    col = row.column()
                    col.operator('tween_follow.remove_tween_target',
                                 text='', icon='X', emboss=False).tween_target_index = i

                row = box.row()
                row.operator('tween_follow.add_tween_target',
                             text='ADD', icon='ADD')
