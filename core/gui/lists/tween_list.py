import bpy

from bpy.types import PropertyGroup
from bpy.types import UIList, UILayout
from bpy.props import StringProperty, IntProperty, CollectionProperty

from ....core.common import Registerable, PropertyHolder


class TWEEN_UL_Target_List_Item(PropertyGroup):
    tween_target: bpy.props.PointerProperty(
        type=bpy.types.Object, name='tween_target')


class TWEEN_UL_List_Item(PropertyGroup):
    tween_source: bpy.props.PointerProperty(
        type=bpy.types.Object, name='tween_source')
    tween_target_list: CollectionProperty(
        name='tween_target_list',
        type=TWEEN_UL_Target_List_Item,
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

    def draw_item(self, context, layout: UILayout, data, item: TWEEN_UL_List_Item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            obj = item.tween_source
            if obj is not None:
                layout.label(text=obj.name)
            else:
                layout.label(text='No source selected')

    @classmethod
    def draw(cls, list_id: str, context, layout: UILayout):
        layout.template_list(cls.__name__, list_id, context.scene,
                             cls.tween_list_items.name, context.scene, cls.tween_list_index.name)
