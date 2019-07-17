#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#
# Authors:
# - Stefan Profanter (profanter@fortiss.org)
#

import logging
import codecs
import sys
import xml.dom.minidom as dom
import json
logger = logging.getLogger(__name__)

class CttSelection:
    """Class containing all selected conformance groups and units of a CTT run"""

    def __init__(self):
        self.projectInfo = ProjectInfo()
        self.conformanceGroups = []

    def parseFile(self, selectionFile, serverProfiles, clientProfiles):
        logger.info("Parsing selection: {}".format(selectionFile.name))
        self.__init__()


        fileContent = selectionFile.read()
        # Remove BOM since the dom parser cannot handle it on python 3 windows
        if fileContent.startswith( codecs.BOM_UTF8 ):
            fileContent = fileContent.lstrip( codecs.BOM_UTF8 )
        if (sys.version_info >= (3, 0)):
            fileContent = fileContent.decode("utf-8")

        uaSelection = dom.parseString(fileContent).getElementsByTagName("UaTestCaseSelection")[0]

        self.projectInfo.parseXml(uaSelection.getElementsByTagName("ProjectInfo")[0])

        profiles = None

        if self.projectInfo.type == "ServerProject":
            profiles = serverProfiles
        elif self.projectInfo.type == "ClientProject":
            profiles = clientProfiles


        for groupsXml in uaSelection.getElementsByTagName("ConformanceGroups")[0].childNodes:
            if groupsXml.nodeType != groupsXml.ELEMENT_NODE:
                continue
            group = SelectedConformanceGroup()
            group.parseXml(groupsXml, profiles)
            self.conformanceGroups.append(group)

        logger.debug("Profile file parsed.")

        #print(json.dumps(mapping_bugs, indent=4))

        return profiles

class ProjectInfo:
    """Class containing the project info of a selection file"""

    def __init__(self):
        self.type = None
        self.version = None

    def parseXml(self, xmlelement):
        self.type = xmlelement.getAttribute("ProjectType")
        self.version = xmlelement.getAttribute("Version")

class SelectedConformanceGroup:

    def __init__(self):
        self.group = None
        self.selectedUnits = []

    def parseXml(self, xmlelement, profiles):

        self.group = profiles.getConformanceGroup(xmlelement.getAttribute("name"))

        for unitXml in xmlelement.getElementsByTagName("ConformanceUnit"):
            if unitXml.nodeType != unitXml.ELEMENT_NODE:
                continue
            unit = SelectedConformanceUnit()
            unit.parseXml(unitXml, profiles, self.group)
            if unit._correctedGroup:
                self.group = unit._correctedGroup
            self.selectedUnits.append(unit)

class SelectedConformanceUnit:

    def __init__(self):
        self.unit = None
        self.selectedTests = []
        self._correctedGroup = None

    def parseXml(self, xmlelement, profiles, group):

        self.unit = group.getConformanceUnit(xmlelement.getAttribute("name"), showWarning=False)

        if not self.unit:
            self._correctedGroup = profiles.getConformanceGroupForUnit(xmlelement.getAttribute("name"))
            self.unit = self._correctedGroup.getConformanceUnit(xmlelement.getAttribute("name"))

        for testXml in xmlelement.getElementsByTagName("TestCases")[0].childNodes:
            if testXml.nodeType != testXml.ELEMENT_NODE:
                continue

            self.selectedTests.append(self.unit.getTest(testXml.getAttribute("name")))
