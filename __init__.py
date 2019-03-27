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

bl_info = {
    "name" : "F3b",
    "author" : "Riccardo Balbo",
    "version": (1,0,0),
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "",
    "category" : "Import-Export"
}

import os,sys,bpy

_modules_path = os.path.join(os.path.dirname(__file__), "libs")
for path in os.listdir(_modules_path):
    p=os.path.join(_modules_path,path)
    print("Load library ",p)
    sys.path.append(p)
# del _modules_path

# _modules_path = os.path.join(os.path.dirname(__file__), "libs")
# for root,subdirs,files in os.walk(_modules_path):
#     for path in subdirs:
#         p=os.path.join(root,path)
#         print("Load library ",str(p))
#         sys.path.append(p)

# sys.path.append(os.path.join(os.path.dirname(__file__), "exporters"))
# sys.path.append(os.path.dirname(__file__))


from . import F3bExporterOperator

modules=[
    F3bExporterOperator
]

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in modules:
        mod.unregister()
    