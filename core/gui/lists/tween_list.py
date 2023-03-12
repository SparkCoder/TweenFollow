import bpy

from bpy.types import PropertyGroup
from bpy.types import UIList, UILayout, Context
from bpy.props import CollectionProperty, PointerProperty, EnumProperty, IntProperty, BoolProperty

from ....core.common import Registerable, PropertyHolder


class TWEEN_UL_Target_List_Item(PropertyGroup):
    tween_target: PointerProperty(
        type=bpy.types.Object,
        name='tween_target'
    )


class TWEEN_UL_List_Item(PropertyGroup):
    tween_source: PointerProperty(
        type=bpy.types.Object,
        name='tween_source',
    )
    tween_target_list: CollectionProperty(
        name='tween_target_list',
        type=TWEEN_UL_Target_List_Item,
    )
    tween_target_coll: PointerProperty(
        type=bpy.types.Object,
        name='tween_target_coll',
    )
    tween_target_type: EnumProperty(
        name='Tween Target Type',
        items=(
            ('Objs', 'Objects', 'Use a list of objects as target'),
            ('Coll', 'Collection', 'Use a collection as target'),
        ),
        default='Objs',
    )
    use_tween: BoolProperty(
        name='use_tween',
        default=True
    )


class TWEEN_UL_List(UIList, Registerable):
    tween_list_index = PropertyHolder(
        name='tween_list_index',
        property=IntProperty(
             name='tween_list_index',
             description='Index for TweenList',
        )
    )
    tween_list_items = PropertyHolder(
        name='tween_list_items',
        property=CollectionProperty(
            name='tween_list_items',
            type=TWEEN_UL_List_Item,
        )
    )

    @classmethod
    def register_cls(cls):
        # Register property dependency classes
        bpy.utils.register_class(TWEEN_UL_Target_List_Item)
        bpy.utils.register_class(TWEEN_UL_List_Item)
        # Register properties
        setattr(bpy.types.Scene, cls.tween_list_index.name,
                cls.tween_list_index.property)
        setattr(bpy.types.Scene, cls.tween_list_items.name,
                cls.tween_list_items.property)
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)
        # Unregister properties
        delattr(bpy.types.Scene, cls.tween_list_items.name)
        delattr(bpy.types.Scene, cls.tween_list_index.name)
        # Unregister property dependency classes
        bpy.utils.unregister_class(TWEEN_UL_List_Item)
        bpy.utils.unregister_class(TWEEN_UL_Target_List_Item)

    def draw_item(self, context: Context, layout: UILayout, data, item: TWEEN_UL_List_Item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            obj = item.tween_source
            if obj is not None:
                layout.label(text=obj.name)
            else:
                layout.label(text=f'{index+1}) No source selected')
            layout.prop(item, 'use_tween', text='')

    @classmethod
    def draw(cls, list_id: str, context: Context, layout: UILayout):
        layout.template_list(cls.__name__, list_id, context.scene,
                             cls.tween_list_items.name, context.scene, cls.tween_list_index.name)
