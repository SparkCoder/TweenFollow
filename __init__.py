# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from .gui.panels.pnl_main import EF_PT_Panel
from .operators.op_apply_all import EF_OT_Apply_All_Op
from .operators.op_cancel_all import EF_OT_Cancel_All_Op

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

operators = (EF_OT_Apply_All_Op, EF_OT_Cancel_All_Op)
guis = (EF_PT_Panel,)


def register():
    # Register operators
    for operator in operators:
        bpy.utils.register_class(operator)
    # Register guis
    for gui in guis:
        # Register properties
        for (prop_name, prop_value) in gui.props.items():
            setattr(bpy.types.Scene, prop_name, prop_value)
        bpy.utils.register_class(gui)


def unregister():
    # Unregister operators
    for operator in operators:
        bpy.utils.unregister_class(operator)
    # Unregister guis
    for gui in guis:
        bpy.utils.unregister_class(gui)
        # Unregister properties
        for prop_name in gui.props.keys():
            delattr(bpy.types.Scene, prop_name)
