import bpy

from typing import List

from .core import EventHandler

from .core.gui import TWEEN_UL_List
from .core.gui import TWEEN_PT_Panel_Main

from .core.operators import TWEEN_OT_Start_Tweens_Op
from .core.operators import TWEEN_OT_Stop_Tweens_Op
from .core.operators import TWEEN_OT_Reset_Tweens_Op
from .core.operators import TWEEN_OT_Add_Tween_Op
from .core.operators import TWEEN_OT_Remove_Tween_Op
from .core.operators import TWEEN_OT_Add_Tween_Target_Op
from .core.operators import TWEEN_OT_Remove_Tween_Target_Op

from .core.common import Registerable

bl_info = {
    'name': 'TweenFollow',
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
    TWEEN_OT_Start_Tweens_Op,
    TWEEN_OT_Stop_Tweens_Op,
    TWEEN_OT_Reset_Tweens_Op,
    TWEEN_OT_Add_Tween_Op,
    TWEEN_OT_Remove_Tween_Op,
    TWEEN_OT_Add_Tween_Target_Op,
    TWEEN_OT_Remove_Tween_Target_Op,
]


def register():
    # Register operators
    for operator in op_registry:
        operator.register_cls()
    # Register guis
    for gui in gui_registry:
        gui.register_cls()
    # Register events
    EventHandler.register_cls()


def unregister():
    # Unregister events
    EventHandler.unregister_cls()
    # Unregister guis
    for gui in gui_registry:
        gui.unregister_cls()
    # Unregister operators
    for operator in op_registry:
        operator.unregister_cls()
