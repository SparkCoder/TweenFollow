import bpy

from bpy.types import Panel


class EF_PT_Panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ease Follow'
    bl_category = 'Ease Follow'

    props = {
        'test': bpy.props.IntProperty(
            name='My Int Property',
            description='An int prop'
        )
    }

    def __init__(self) -> None:
        super().__init__()

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
