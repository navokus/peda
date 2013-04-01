#
# PEDA - Python Exploit Development Assistance for GDB
#
# Copyright (C) 2013 - Navokus 
#
# License: see LICENSE file for details
#
"""
Simple IDAPython script to export function name to file

Usage:
   Python>execfile("/path/to/exportname.py")
   Python>export_local_function()

"""
from idautils import *
from idaapi import *


def export_local_function():
    local_f = list(Names())
    file_s = get_root_filename() + ".s"
    fd = open(file_s, 'w')
    for f in local_f:
        fd.write("%s 0x%x\n"%(f[1], f[0]))
    fd.close()
    print "Exported to %s" % (file_s)
        
print "Usage: export_local_function()"
    
