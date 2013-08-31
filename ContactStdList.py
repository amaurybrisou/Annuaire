#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Utils
import pickle as pickle
import Configuration

class ContactStd:
    
    def __init__(self, config):
        if not isinstance(config, Configuration.Configuration):
            raise TypeError("ContactList need a Configuration Class in argument")

        if Utils.CheckOldFormat(config, type(self)) == True:
            super().__init__()
        else:
            try:
                super().__init__(pickle.load(open(config.get("MAIN", "filename") , "rb")))
            except IOError:
                print("Aucun Fichier")
        
        
    def append(self, obj):
        super().append(obj)
        
    def __getstate__(self):
        contact_list_attr = self.__dict__.copy()
        return contact_list_attr
        
    def __setstate__(self, state):
        self.__dict__ = state
