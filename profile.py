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
from result import TestResult

class Profiles:
    """Class containing all profiles of a project"""

    def __init__(self):
        self.categories = []
        self.projectInfo = ProjectInfo()
        self.conformanceGroups = []
        self.profiles = []
        self.result = []
        self.accumulatedTestResult = None

    def parseFile(self, profilesFile):
        logger.info("Parsing profiles: {}".format(profilesFile.name))
        self.__init__()


        fileContent = profilesFile.read()
        # Remove BOM since the dom parser cannot handle it on python 3 windows
        if fileContent.startswith( codecs.BOM_UTF8 ):
            fileContent = fileContent.lstrip( codecs.BOM_UTF8 )
        if (sys.version_info >= (3, 0)):
            fileContent = fileContent.decode("utf-8")

        uaProfile = dom.parseString(fileContent).getElementsByTagName("UaProfiles")[0]

        self.projectInfo.parseXml(uaProfile.getElementsByTagName("ProjectInfo")[0])

        for categoryXml in uaProfile.getElementsByTagName("Categories")[0].childNodes:
            if categoryXml.nodeType != categoryXml.ELEMENT_NODE:
                continue
            cat = ProfileCategory()
            cat.parseXml(categoryXml)
            self.categories.append(cat)

        for groupsXml in uaProfile.getElementsByTagName("ConformanceGroups")[0].childNodes:
            if groupsXml.nodeType != groupsXml.ELEMENT_NODE:
                continue
            group = ConformanceGroup()
            group.parseXml(groupsXml, self)
            self.conformanceGroups.append(group)

        for profilesXml in uaProfile.getElementsByTagName("Profiles")[0].childNodes:
            if profilesXml.nodeType != profilesXml.ELEMENT_NODE:
                continue
            profile = Profile()
            profile.parseXml(profilesXml, self)
            self.profiles.append(profile)

        for profile in self.profiles:
            profile.delayInit(self)

        logger.debug("Profile file parsed.")

        #print(json.dumps(mapping_bugs, indent=4))


    def getCategory(self, categoryName):
        for cat in self.categories:
            if cat.name == categoryName:
                return cat
        logger.warning("Category '{}' not found.".format(categoryName))
        return None

    def getConformanceGroup(self, groupName):
        for grp in self.conformanceGroups:
            if grp.name == groupName:
                return grp
        logger.warning("ConformanceGroup '{}' not found.".format(groupName))
        return None

    def getConformanceGroupForUnit(self, unitName):
        for grp in self.conformanceGroups:
            unit = grp.getConformanceUnit(unitName, showWarning=False)
            if unit:
                return grp
        return None

    def getProfile(self, profileName, showWarning=False):
        for profile in self.profiles:
            if profile.name == profileName:
                return profile
        if showWarning:
            logger.warning("Profile '{}' not found.".format(profileName))
        return None

class ProjectInfo:
    """Class containing the project info of a profiles file"""

    def __init__(self):
        self.type = None
        self.profile = None
        self.scriptVersion = None
        self.version = None

    def parseXml(self, xmlelement):
        self.type = xmlelement.getAttribute("ProjectType")
        self.profile = xmlelement.getAttribute("ProjectProfile")
        self.scriptVersion = xmlelement.getAttribute("ScriptVersion")
        self.version = xmlelement.getAttribute("Version")


class ProfileCategory:
    """Class describing the profile category"""

    def __init__(self):
        self.description = None
        self.name = None

    def parseXml(self, xmlelement):
        self.description = xmlelement.getAttribute("description")
        self.name = xmlelement.getAttribute("name")


class ConformanceGroup:
    """A Conformance group groups together one or multiple conformance units"""

    def __init__(self):
        self.conformanceUnits = []
        self.description = None
        self.name = None
        self.result = []
        self.accumulatedTestResult = None

    def parseXml(self, xmlelement, profiles):
        self.description = xmlelement.getAttribute("description")
        self.name = xmlelement.getAttribute("name")

        for unitXml in xmlelement.getElementsByTagName("ConformanceUnits")[0].childNodes:
            if unitXml.nodeType != unitXml.ELEMENT_NODE:
                continue
            unit = ConformanceUnit()
            unit.parseXml(unitXml, profiles)
            self.conformanceUnits.append(unit)

    def getConformanceUnit(self, unitName, showWarning=True):
        for unit in self.conformanceUnits:
            if unit.name == unitName:
                return unit
        if showWarning:
            logger.warning("ConformanceUnit '{}' inside group '{}' not found.".format(unitName, self.name))
        return None


    def getResult(self):
        if self.accumulatedTestResult:
            return self.accumulatedTestResult

        if self.result and len(self.result) > 0:
            self.accumulatedTestResult = self.result.testresult
        else:
            self.accumulatedTestResult = TestResult.UNKNOWN
            for unit in self.conformanceUnits:
                res = unit.getResult()
                if res < self.accumulatedTestResult:
                    self.accumulatedTestResult = res

        return self.accumulatedTestResult

class ConformanceUnit:
    """A conformance unit contains test cases"""

    def __init__(self):
        self.category = None
        self.description = None
        self.name = None
        self.used = None
        self.testCases = []
        self.initTestCase = None
        self.cleanupTestCase = None
        self.result = []
        self.accumulatedTestResult = None

    def parseXml(self, xmlelement, profiles):
        self.description = xmlelement.getAttribute("description")
        self.name = xmlelement.getAttribute("name")
        self.used = xmlelement.getAttribute("used") == "true"
        cat = xmlelement.getAttribute("category")
        self.category = profiles.getCategory(cat) if cat is not '' else None

        if len(xmlelement.getElementsByTagName("InitTestCase")) > 0:
            self.initTestCase = TestCase()
            self.initTestCase.parseXml(xmlelement.getElementsByTagName("InitTestCase")[0])

        if len(xmlelement.getElementsByTagName("CleanupTestCase")) > 0:
            self.cleanupTestCase = TestCase()
            self.cleanupTestCase.parseXml(xmlelement.getElementsByTagName("CleanupTestCase")[0])

        for testXml in xmlelement.getElementsByTagName("TestCases")[0].childNodes:
            if testXml.nodeType != testXml.ELEMENT_NODE:
                continue
            testCase = TestCase()
            testCase.parseXml(testXml)
            self.testCases.append(testCase)

    def getTest(self, testName, showWarning=True):
        for test in self.testCases:
            if test.name == testName:
                return test
        if showWarning:
            logger.warning("Test '{}' inside unit '{}' not found.".format(testName, self.name))
        return None


    def getResult(self):
        if self.accumulatedTestResult:
            return self.accumulatedTestResult

        if self.result and len(self.result) > 0:
            self.accumulatedTestResult = self.result.testresult
        else:
            self.accumulatedTestResult = TestResult.UNKNOWN
            for test in self.testCases:
                res = test.getResult()
                if res < self.accumulatedTestResult:
                    self.accumulatedTestResult = res

        return self.accumulatedTestResult

class TestCase:
    """A single test case within a conformance unit"""

    def __init__(self):
        self.description = None
        self.name = None
        self.filename = None
        self.checkedState = None
        self.result = []
        self.accumulatedTestResult = None

    def parseXml(self, xmlelement):
        self.description = xmlelement.getAttribute("description")
        self.name = xmlelement.getAttribute("name")
        self.filename = xmlelement.getAttribute("filename")
        self.checkedState = xmlelement.getAttribute("checkedState")

    def getResult(self):
        if self.accumulatedTestResult:
            return self.accumulatedTestResult

        if self.result:
            self.accumulatedTestResult = self.result.testresult
        else:
            self.accumulatedTestResult = TestResult.SKIPPED

        return self.accumulatedTestResult

mapping_bugs = {}

class IncludedConformanceUnit:
    """Metadata for included conformance unit inside a profile"""

    def __init__(self):
        self.optional = None
        self.group = None
        self.unit = None

    def parseXml(self, xmlelement, profiles, parentProfile, profile_mapping_bugs=None):
        self.optional = xmlelement.getAttribute("optional") == "true"


        groupName = xmlelement.getAttribute("group")
        unitName = xmlelement.getAttribute("name")

        self.group = profiles.getConformanceGroup(groupName)
        self.unit = self.group.getConformanceUnit(unitName, showWarning=False)

        # There are some bugs in the uaprofile file where conformance units are not mapped to the correct conformance group.
        # Try to fix this by searching the correct group here
        if not self.unit:
            map = mapping_bugs[parentProfile.name] if parentProfile.name in mapping_bugs else {}

            units = map['units'] if 'units' in map else {}

            self.group = profiles.getConformanceGroupForUnit(unitName)

            units[unitName] = {
                "wrongGroup": groupName,
                "correctGroup": self.group.name
            }

            map['units'] = units

            mapping_bugs[parentProfile.name] = map

            self.unit = self.group.getConformanceUnit(unitName)


class Profile:
    """A profile which includes conformance units and other profiles """

    def __init__(self):
        self.category = None
        self.description = None
        self.name = None
        self.uri = None
        self.isFacet = None
        self.conformanceUnits = []
        self.profiles = []
        self._delay_profile_add = []
        self.accumulatedTestResult = None

    def parseXml(self, xmlelement, profiles):
        self.category = profiles.getCategory(xmlelement.getAttribute("category"))
        self.description = xmlelement.getAttribute("description")
        self.name = xmlelement.getAttribute("name")
        self.uri = xmlelement.getAttribute("uri")
        self.isFacet = self.name.endswith("Facet")

        for includeUnitsXml in xmlelement.getElementsByTagName("IncludeConformanceUnits")[0].childNodes:
            if includeUnitsXml.nodeType != includeUnitsXml.ELEMENT_NODE:
                continue
            includeUnit = IncludedConformanceUnit()
            includeUnit.parseXml(includeUnitsXml, profiles, self)
            self.conformanceUnits.append(includeUnit)

        for includeProfileXml in xmlelement.getElementsByTagName("IncludeProfiles")[0].childNodes:
            if includeProfileXml.nodeType != includeProfileXml.ELEMENT_NODE:
                continue
            profile = profiles.getProfile(includeProfileXml.getAttribute("name"))
            if profile:
                self.profiles.append(profile)
            else:
                self._delay_profile_add.append(includeProfileXml.getAttribute("name"))

    def delayInit(self, profiles):
        for includeProfileName in self._delay_profile_add:
            profile = profiles.getProfile(includeProfileName, showWarning=True)
            if profile:
                self.profiles.append(profile)
        self._delay_profile_add = []


    def getResult(self):
        if self.accumulatedTestResult:
            return self.accumulatedTestResult

        self.accumulatedTestResult = TestResult.UNKNOWN
        for selUnit in self.conformanceUnits:
            if selUnit.optional:
                continue
            res = selUnit.unit.getResult()
            if res < self.accumulatedTestResult:
                self.accumulatedTestResult = res

        for profile in self.profiles:
            res = profile.getResult()
            if res < self.accumulatedTestResult:
                self.accumulatedTestResult = res

        return self.accumulatedTestResult
