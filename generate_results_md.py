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
import argparse
from profile import *
from result import *
from selection import *
import json

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-r', '--results',
                    metavar="<resultsFile>",
                    type=argparse.FileType('rb'),
                    default='example.results.xml',
                    help='results.xml file path containing the CTT results')

parser.add_argument('-s', '--selection',
                    metavar="<selectionFile>",
                    type=argparse.FileType('rb'),
                    default='example.selection.xml',
                    help='selection.xml file path containing the CTT results')

parser.add_argument('--profilesServer',
                    metavar="<profilesServerFile>",
                    type=argparse.FileType('rb'),
                    default='./CTT/ServerProjects/Standard/uaprofiles.xml',
                    help='uaprofiles.xml file which contains all the possible profiles and conformance units of a Server')

parser.add_argument('--profilesClient',
                    metavar="<profilesClientFile>",
                    type=argparse.FileType('rb'),
                    default='./CTT/ClientProjects/Standard/uaprofiles.xml',
                    help='uaprofiles.xml file which contains all the possible profiles and conformance units of a Server')

parser.add_argument('--configClient',
                    metavar="<configClient>",
                    type=argparse.FileType('rb'),
                    default='client.status.json',
                    help='status.json file which contains additional implementation status information for the Client units')

parser.add_argument('--configServer',
                    metavar="<configServer>",
                    type=argparse.FileType('rb'),
                    default='server.status.json',
                    help='status.json file which contains additional implementation status information for the Server units')

parser.add_argument('--header',
                    metavar="<templateHeader>",
                    type=argparse.FileType('rb'),
                    default='template_header.md',
                    help='File which content will be added at the beginning of the resulting .md file')

parser.add_argument('--footer',
                    metavar="<templateFooter>",
                    type=argparse.FileType('rb'),
                    default='template_footer.md',
                    help='File which content will be added at the end of the resulting .md file')

parser.add_argument('-v', '--verbose', action='count',
                    default=1,
                    help='Make the script more verbose. Can be applied up to 4 times')

parser.add_argument('--format',
                    default='markdown',
                    const='markdown',
                    nargs='?',
                    choices=['markdown'],
                    help='Format for the output file (default: %(default)s)')

parser.add_argument('outputFile',
                    metavar='<outputFile>',
                    default='PROFILES.md',
                    help='The path to the output file')


args = parser.parse_args()

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
verbosity = 0
if args.verbose:
    verbosity = int(args.verbose)
if (verbosity == 1):
    logging.basicConfig(level=logging.ERROR)
elif (verbosity == 2):
    logging.basicConfig(level=logging.WARNING)
elif (verbosity == 3):
    logging.basicConfig(level=logging.INFO)
elif (verbosity >= 4):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.CRITICAL)

serverStatus = json.loads(args.configServer.read().decode("utf-8"))
clientStatus = json.loads(args.configClient.read().decode("utf-8"))

serverProfiles = Profiles()
serverProfiles.parseFile(args.profilesServer)
serverProfiles.setImplementationStatus(serverStatus)

clientProfiles = Profiles()
clientProfiles.parseFile(args.profilesClient)
clientProfiles.setImplementationStatus(clientStatus)

selection = CttSelection()
selectedProfilesType = selection.parseFile(args.selection, serverProfiles=serverProfiles, clientProfiles=clientProfiles)

results = CttResults()
results.parseFileResultsIntoSelection(args.results, selection)


logger.info("Generating output with format: {}".format(args.format))

if args.format == "markdown":
    from format_markdown import write_format_markdown
    write_format_markdown(selectedProfilesType, selection, results, args.outputFile, args.header, args.footer)
else:
    logger.error("Unsupported backend: {}".format(args.backend))
    exit(1)

logger.info("Output file generated")

exit(0)



