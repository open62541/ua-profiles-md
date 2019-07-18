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
logger = logging.getLogger(__name__)
from enum import IntEnum

class ImplementationStatus(IntEnum):
    UNKNOWN = 0
    NOT_IMPLEMENTED = 1
    BEING_IMPLEMENTED = 2
    INCUBATING = 3
    STABLE = 4
    CERTIFIED = 5
