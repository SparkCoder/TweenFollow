import bpy

from typing import List

from .core.gui import TWEEN_UL_List_Item
from .core.gui import TWEEN_UL_List
from .core.gui import TWEEN_PT_Panel_Main

from .core.operators import EF_OT_Apply_All_Op
from .core.operators import EF_OT_Cancel_All_Op

from .core.common import Registerable

bl_info = {
    'name': 'EaseFollow',
    'author': 'SparkCoder',
    'description': '',
    'blender': (2, 80, 0),
    'version': (0, 0, 1),
    'location': 'View3D',
    'warning': '',
    'category': 'Object'
}


gui_registry: List[Registerable] = [
    TWEEN_UL_List,
    TWEEN_PT_Panel_Main,
]
op_registry: List[Registerable] = [
    EF_OT_Apply_All_Op,
    EF_OT_Cancel_All_Op,
]


def register():
    # Register operators
    for operator in op_registry:
        operator.register_cls()
    # Register guis
    for gui in gui_registry:
        gui.register_cls()


def unregister():
    # Unregister operators
    for operator in op_registry:
        operator.unregister_cls()
    # Unregister guis
    for gui in gui_registry:
        gui.unregister_cls()
