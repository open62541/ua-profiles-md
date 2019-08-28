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
logger = logging.getLogger(__name__)
from enum import IntEnum
from dateutil.parser import parse

class CttResults:
    """Class grouping all the CTT results"""

    def __init__(self):
        self.runs = []

    def parseFileResultsIntoSelection(self, profilesFile, cttSelection):
        logger.info("Parsing results: {}".format(profilesFile.name))
        self.__init__()


        fileContent = profilesFile.read()
        # Remove BOM since the dom parser cannot handle it on python 3 windows
        if fileContent.startswith( codecs.BOM_UTF8 ):
            fileContent = fileContent.lstrip( codecs.BOM_UTF8 )
        if (sys.version_info >= (3, 0)):
            fileContent = fileContent.decode("utf-8")

        cttResults = dom.parseString(fileContent).getElementsByTagName("UaCttResults")[0]

        for xmlElement in cttResults.childNodes:
            if xmlElement.nodeType != xmlElement.ELEMENT_NODE:
                continue
            result = Result()
            result.parseXml(xmlElement)
            self.runs.append(result)


        if len(self.runs) < 1:
            logger.error("Results file does not contain any run.")
            return
        elif len(self.runs) > 1:
            logger.error("Results file contains more than one run. Only considering the first one.")

        run = self.runs[0]
        self.setResultsForSelectedConformanceGroups(run, cttSelection)

    def setResultsForSelectedConformanceGroups(self, runResults, cttSelection):

        for selGroup in cttSelection.conformanceGroups:
            groupResults = None
            for res in runResults.results:
                if res.name == selGroup.group.name:
                    groupResults = res
                    break
            if not groupResults:
                logger.error("Did not find result nodes for group {}".format(selGroup.name))
                break

            selGroup.result = groupResults
            self.setResultsForSelectedUnits(selGroup)

    def setResultsForSelectedUnits(self, group):
        for selUnit in group.selectedUnits:
            unitResults = None
            for res in group.result.results:
                if res.name == selUnit.unit.name:
                    unitResults = res
                    break
            if not unitResults:
                logger.error("Did not find result nodes for unit {}".format(selUnit.name))
                break

            selUnit.result = unitResults

            self.setResultsForSelectedTests(selUnit)

    def setResultsForSelectedTests(self, unit):
        for selTest in unit.selectedTests:
            if not selTest:
                continue
            testResults = None
            for res in unit.result.results:
                if res.name == selTest.name:
                    testResults = res
                    break
            if not testResults:
                logger.error("Did not find result nodes for test {}".format(selTest.name))
                break

            selTest.result = testResults

class TestResult(IntEnum):
    ERROR = 0
    WARNING = 1
    NOT_IMPLEMENTED = 2
    SKIPPED = 3
    NOT_SUPPORTED = 4
    OK = 5
    BACK_TRACE = 6
    UNKNOWN = 99


class Result:
    """Class describing the result of a CTT test and grouping sub-results"""

    def __init__(self):
        self.status = None
        self.description = None
        self.testresult = None
        self.timestamp = None
        self.name = None
        self.results = []

    def parseXml(self, xmlelement):


        testresult_map = {
            "0": TestResult.ERROR,
            "1": TestResult.WARNING,
            "2": TestResult.NOT_IMPLEMENTED,
            "3": TestResult.SKIPPED,
            "4": TestResult.NOT_SUPPORTED,
            "5": TestResult.OK,
            "6": TestResult.BACK_TRACE
        }

        self.status = xmlelement.getAttribute("status")
        self.description = xmlelement.getAttribute("description")
        self.testresult = testresult_map[xmlelement.getAttribute("testresult")]

        self.timestamp = parse(xmlelement.getAttribute("timestamp"))


        self.name = xmlelement.getAttribute("name")

        for subElement in xmlelement.childNodes:
            if subElement.nodeType != subElement.ELEMENT_NODE:
                continue
            result = Result()
            result.parseXml(subElement)
            self.results.append(result)
