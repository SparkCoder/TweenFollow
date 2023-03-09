import bpy

from .core import gui_registry
from .core import op_registry

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
