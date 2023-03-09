import bpy

from bpy.types import Panel, PropertyGroup
from bpy.props import StringProperty, IntProperty, CollectionProperty

from . import Registerable, gui_registry

import inspect


class CustomPropertiesGroup(PropertyGroup):
    customString: StringProperty(name='', default='')


class EF_PT_Panel(Panel, Registerable):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ease Follow'
    bl_category = 'Ease Follow'

    props = {
        'test1': IntProperty(
            update=lambda self, context: EF_PT_Panel.update(),
            name='My Int Property',
            description='An int prop'
        ),
        'test2':  CollectionProperty(
            type=CustomPropertiesGroup
        )
    }

    @classmethod
    def update(cls):
        ctx = bpy.data.scenes[0]

        ctx.test1 = ctx.test1 if ctx.test1 >= 0 else 0

        ctx.test2.clear()
        for i in range(ctx.test1):
            item = ctx.test2.add()
            item.customString = 'test' + str(i+1)

    @classmethod
    def register_cls(cls):
        # Register custom properties
        bpy.utils.register_class(CustomPropertiesGroup)
        # Register properties
        for (prop_name, prop_value) in cls.props.items():
            setattr(bpy.types.Scene, prop_name, prop_value)
        # Register class
        bpy.utils.register_class(cls)

    @classmethod
    def unregister_cls(cls):
        # Unregister class
        bpy.utils.unregister_class(cls)
        # Unregister properties
        for prop_name in cls.props.keys():
            delattr(bpy.types.Scene, prop_name)
        # Unregister custom properties
        bpy.utils.unregister_class(CustomPropertiesGroup)

    def draw(self, context):
        layout = self.layout

        row = layout.row()

        col = row.column()
        col.operator('object.apply_all_mods', text='App1y all')

        col = row.column()
        col.operator('object.cancel_all_mods', text='Cancel all')

        row = layout.row()
        col = row.column()
        for prop_name in self.props.keys():
            row = col.row()
            row.prop(context.scene, prop_name)

        row = layout.row()
        col = row.column()
        for i in range(len(context.scene.test2)):
            li_la = col.label(text=context.scene.test2[i].customString)


gui_registry += [EF_PT_Panel]
