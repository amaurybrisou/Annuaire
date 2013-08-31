#! /usr/bin/env python3


#import FileManager as FM
from KeyboardParser import KeyboardParser
import Helps
import Utils
import os
from Configuration import Configuration

config = Configuration()

annuaire_type = config.get("MAIN", "type")

ChoosenListType = Utils.getClass(annuaire_type)

contacts = ChoosenListType(config)

Helps.welcome()

parser = KeyboardParser(contacts, config, ChoosenListType)

os._exit(0)
