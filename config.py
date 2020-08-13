# -*- coding: utf-8 -*-
"""
Beautify Anki
an Addon for Anki
Github (https://github.com/my-Anki/Beautify-Anki)
Copyright (c) 2020 Shorouk Abdelaziz (https://shorouk.dev)
"""
#################################################################################
# Beautify Anki n is released under GNU AGPL, version 3 or later                #
# This Addon uses the following CSS and Javascript libraries                    #
#                                                                               #
# Acknowledgments                                                               #
# This Addon uses the following CSS and Javascript libraries                    #
#   - Materialize                                                               #
#   - Animate.css                                                               #
#   - plotly                                                                    #
# The Statistics part in the Deck Browser is based on Carlos Duarte             #
#  addon "More Decks Stats and Time Left" which is based on                     #
#  Dmitry Mikheev code, in add-on "More decks overview stats"                   #
#  and calumks code, in add-on "Deck Stats"                                     #
#                                                                               #
# The Statistics part in The Deck Overview pages is based on                    #
#  Kazuwuqt addon "More Overview Stats 2.1 " which is based on                  #
#  the More Overview Stats 2 add-on by Martin Zuther which is in turn based on  #
#  "More Overview Stats" by Calumks                                             #
#                                                                               #
#################################################################################

from aqt import mw
import os , sys
from aqt.utils import showInfo
from aqt.theme import theme_manager
import json



NIHGT_MODE = theme_manager.night_mode
CONFIG = mw.addonManager.getConfig(__name__)

ADDON = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
USERTHEMEFILE = ADDON+"/theme_settings/"+CONFIG["theme"]+'.json'

with open(USERTHEMEFILE) as json_file:
    THEME = json.load(json_file)

    BROWSER = THEME["DECK-BROWSER"]
    PIE = THEME["DECK-OVERVIEW"]["PIE-CHART"]
    OVERVIEW =THEME["DECK-OVERVIEW"]
    change_in_night = ["large-areas-color","decks-border-color","decks-color","filtered-deck-color"]
    if CONFIG["theme"] == "default" and NIHGT_MODE:
        for value in change_in_night :
            THEME[value] = THEME["night"][value]



LOCALS= CONFIG["local"]

