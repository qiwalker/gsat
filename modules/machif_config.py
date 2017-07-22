"""----------------------------------------------------------------------------
   machif_config.py

   Copyright (C) 2013-2017 Wilhelm Duembeg

   This file is part of gsat. gsat is a cross-platform GCODE debug/step for
   Grbl like GCODE interpreters. With features similar to software debuggers.
   Features such as breakpoint, change current program counter, inspection
   and modification of variables.

   gsat is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 2 of the License, or
   (at your option) any later version.

   gsat is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with gsat.  If not, see <http://www.gnu.org/licenses/>.

----------------------------------------------------------------------------"""

import modules.config as gc
import modules.machif as mi
import modules.g2core_machif as mi_g2core
import modules.tinyg_machif as mi_tinyg
import modules.grbl_machif as mi_grbl

# --------------------------------------------------------------------------
# device commands
# --------------------------------------------------------------------------
gMACHIF_CMD_GO_TO_POS         = "G00"     # G00 <AXIS><VAL>
gMACHIF_CMD_SPINDLE_ON        = "M3"
gMACHIF_CMD_SPINDLE_OFF       = "M5"
gMACHIF_CMD_HOME_AXIS         = "G28.2"   # G28.2 <AXIS>0
gMACHIF_CMD_SET_AXIS          = "G28.3"   # G28.3 <AXIS><VAL>
gMACHIF_CMD_OFFSET_AXIS       = "G92"     # G92 <AXIS><VAL>

# --------------------------------------------------------------------------
# Device type, this data needs to be in sync with the machif_* files
# --------------------------------------------------------------------------
gMACHIF_NONE            = None
#gMACHIF_GRBL            = 1000
#gMACHIF_TINYG           = 1100
#gMACHIF_G2CORE          = 1200

gMachIf_GRBL = mi_grbl.machIf_GRBL(gc.gCmdLineOptions)
gMachIf_TinyG = mi_tinyg.machIf_TinyG(gc.gCmdLineOptions)
gMachIf_g2core = mi_g2core.machIf_g2core(gc.gCmdLineOptions)

gMachIfList = [gMachIf_GRBL.GetName(), gMachIf_TinyG.GetName(), gMachIf_g2core.GetName()]

"""----------------------------------------------------------------------------
   GetMachIfName:
   translate ID to string.
----------------------------------------------------------------------------"""
def GetMachIfName(machIfId):
   machIfName = "None"

   if machIfId == gMachIf_GRBL.GetId():
      machIfName = gMachIf_GRBL.GetName()

   elif machIfId == gMachIf_TinyG.GetId():
      machIfName = gMachIf_TinyG.GetName()

   elif machIfId == gMachIf_g2core.GetId():
      machIfName = gMachIf_g2core.GetName()

   return machIfName

"""----------------------------------------------------------------------------
   GetMachIfId:
   translate string to ID.
----------------------------------------------------------------------------"""
def GetMachIfId(deviceStr):
   machIfId = gMACHIF_NONE

   if deviceStr in [gMachIf_g2core.GetName(), "TinyG2"]:
      machIfId = gMachIf_g2core.GetId()

   elif deviceStr in [gMachIf_GRBL.GetName(), "Grbl", "GRBL"]:
      machIfId = gMachIf_GRBL.GetId()

   elif deviceStr in [gMachIf_TinyG.GetName()]:
      machIfId = gMachIf_TinyG.GetId()

   return machIfId

"""----------------------------------------------------------------------------
   GetMachIfModule:
   translate string to ID.
----------------------------------------------------------------------------"""
def GetMachIfModule(machIfId):
   machIfModule = None

   if machIfId == gMachIf_GRBL.GetId():
      machIfModule = mi_grbl.machIf_GRBL(gc.gCmdLineOptions)

   elif machIfId == gMachIf_TinyG.GetId():
      machIfModule = mi_tinyg.machIf_TinyG(gc.gCmdLineOptions)

   elif machIfId == gMachIf_g2core.GetId():
      machIfModule = mi_g2core.machIf_g2core(gc.gCmdLineOptions)

   return machIfModule
