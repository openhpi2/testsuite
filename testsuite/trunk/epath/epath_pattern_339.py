#!/usr/bin/env python
'''
 (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Suntrupth S Yadav <suntrupth@in.ibm.com>
'''
####################################################################
# Warning: This file is auto-magically generated by:
# gen_epath_pattern_tests.py
# Do not change this file manually. Instead update the script above.
####################################################################

# This takes an entity path and an entity path's pattern,
# and knowing the proper result beforehand, checks if the
# pattern matches the entity path. If the proper result is
# achieved, the test passes.

import unittest
from openhpi import *

class TestSequence(unittest.TestCase):
        
    def runTest(self):
        ep_str = "{SYSTEM_CHASSIS,1}{PHYSICAL_SLOT,4}{SBC_BLADE,3}"
        epp_str = "*{SYSTEM_CHASSIS,.}*{SBC_BLADE,.}*"
        epp = oh_entitypath_pattern()
        ep = SaHpiEntityPathT()
        error = SA_OK
        match = "1"

        error = oh_encode_entitypath(ep_str, ep)
        self.assertEqual  (error == SA_OK,True) 
        
        error = oh_compile_entitypath_pattern(epp_str, epp)
        self.assertEqual(error == SA_OK, True) 
        
        self.assertEqual(oh_match_entitypath_pattern(epp, ep) != match, True)

if __name__=='__main__':
    unittest.main()
