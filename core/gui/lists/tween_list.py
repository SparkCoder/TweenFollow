import bpy

from bpy.types import Panel, PropertyGroup
from bpy.types import UIList, UILayout
from bpy.props import StringProperty, IntProperty, CollectionProperty

from ....core.common import Registerable, PropertyHolder


class TWEEN_UL_List_Item(PropertyGroup):
    customString: StringProperty(name='custom', default='')


class TWEEN_UL_List(UIList, Registerable):
    list_index = PropertyHolder(
        name='TweenList_Index',
        property=IntProperty(
             name='TweenList_Index',
             description='Index for TweenList',
        )
    )
    list_items = PropertyHolder(
        name='TweenList',
        property=CollectionProperty(
            name='TweenList',
            type=TWEEN_UL_List_Item,
        )
    )

    @classmethod
    def register_cls(cls):
        # Register property dependency classes
        bpy.utils.register_class(TWEEN_UL_List_Item)
        # Register properties
        setattr(bpy.types.Scene, cls.list_index.name, cls.list_index.property)
        setattr(bpy.types.Scene, cls.list_items.name, cls.list_items.property)
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)
        # Unregister properties
        delattr(bpy.types.Scene, cls.List_Item.name, cls.List_Item)
        delattr(bpy.types.Scene, cls.list_index.name, cls.list_index)
        # Unregister property dependency classes
        bpy.utils.unregister_class(TWEEN_UL_List_Item)

    @classmethod
    def update(cls):
        ctx = bpy.data.scenes[0]

        ctx.test1 = ctx.test1 if ctx.test1 >= 0 else 0

        ctx.test2.clear()
        for i in range(ctx.test1):
            item = ctx.test2.add()
            item.customString = 'test' + str(i+1)

    def draw_item(self, context, layout: UILayout, data, item: TWEEN_UL_List_Item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.customString)

    @classmethod
    def draw(cls, list_id: str, context, layout: UILayout):
        layout.template_list(cls.__name__, list_id, context.scene,
                             cls.list_items.name, context.scene, cls.list_index.name)
