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
import json
from status import ImplementationStatus
import codecs
import os

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-c', '--config',
                    metavar="<configFile>",
                    default='server.status.json',
                    help='status.json file describing the implementation status of specific conformance units')

parser.add_argument('--profiles',
                    metavar="<profilesFile>",
                    type=argparse.FileType('rb'),
                    default='./CTT/ServerProjects/Standard/uaprofiles.xml',
                    help='uaprofiles.xml file which contains all the possible profiles and conformance units')


parser.add_argument('-v', '--verbose', action='count',
                    default=1,
                    help='Make the script more verbose. Can be applied up to 4 times')

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


profiles = Profiles()
profiles.parseFile(args.profiles)

if os.path.exists(args.config):
    with codecs.open(args.config, "r", encoding='utf-8') as configFile:
        fileContent = configFile.read()
    status = json.loads(fileContent)
else:
    status = {}

addedNewUnits = False

for group in profiles.conformanceGroups:
    if not group.name in status:
        status[group.name] = {}
    map = status[group.name]

    for unit in group.conformanceUnits:
        if not unit.name in map:
            map[unit.name] = ImplementationStatus.UNKNOWN
            addedNewUnits = True

if addedNewUnits:
    with open(args.config, 'w') as outfile:
        json.dump(status, outfile, indent=4, sort_keys=True)
    logger.warning("New units have been added to the config. Please update their status. They are marked as unknown.")
else:
    logger.info("Your config is up-to-date")

exit(0)



