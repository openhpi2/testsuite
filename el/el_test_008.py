#!/usr/bin/env python

"""
 (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Jayashree Padmanabhan <jayshree@in.ibm.com>
"""

import unittest
from openhpi import *


class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
 *
 * This test adds 5 entries to an event log, It then clears the EL and 
 * verifies the event log is actually clear.
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
 
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")
        data.append("Test data two")
        data.append("Test data three")
        data.append("Test data four")
        data.append("Test data five")
        	
        # create a new EL of size 20
        el = oh_el_create(20)

        # add 5 events to el 
        for x in range (0,5):
            event.Source = 1
            event.EventType = SAHPI_ET_USER
            event.Timestamp = SAHPI_TIME_UNSPECIFIED
            event.Severity = SAHPI_DEBUG
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]

            retc = oh_el_append(el, event, None, None)
            if (retc != SA_OK):
                print "ERROR: oh_el_append failed."
                return 1
            x = x+1
            
        # clear the el 
        retc = oh_el_clear(el)
        if (retc != SA_OK):
            print "ERROR: el clear failed."
            return 1
        

        # verify el list nodes are cleared 
        if(el.list != None):
            print "ERROR: el clear failed."
            return 1
    
        # close el without saving to file
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close on el failed."
            return 1
        return 0

if __name__=='__main__':
        unittest.main()  