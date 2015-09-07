#!/usr/bin/env python
__author__ = "The Artha Group"
__date__ = "$Sep 6, 2015 8:38:25 PM$"
__copyright__ = "Copyright 2015, Project Artha"
__credits__ = ["Redhart", "Adnan Khan", "Gurkirpal Singh"]
__license__ = "GPL v2.0"
__version__ = "1.0.1"
__maintainer__ = "Redhart"
__email__ = "teamalpha@mantraloft.com"
__status__ = "Development"

import bot_activity as artha

err = None  # capture errors

artha.bot_call(err)

if err is None:
    artha.bot_control()
