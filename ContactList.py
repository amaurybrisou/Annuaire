#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import Utils
from Contact import Contact
from ContactStdList import ContactStd


class ContactList(ContactStd, list):

    def __init__(self, config):
        super().__init__(config)
        self.maxid = len(self)

    def append(self, firstname, lastname, phone_number):
        super().append( \
            Contact((self.maxid), (firstname), (lastname), (phone_number)))
        self.maxid += 1

    def __str__(self):
        ret = ""
        for i in self:
            ret += str(i)
        return ret

    def index(self, field, value):
        for m in [obj_it for obj_it in self if \
        getattr(obj_it, field) == value]:
            return self[super().index(m)]

    def modify(self, obj, field):
        value = Utils.getNewValue(field)
        [setattr(obj_it, field, value) for obj_it in self if \
        obj_it == obj and \
        (field == "firstname" or "lastname" or "phone_number" and value != "")]

    def flattendIds(self):
        for i, obj in enumerate(self):
            obj.id = i

    def remove(self, field, value):
        os.system('clear')

        def confirmation(obj_it):
            if obj_it != None and Utils.AskForDeletion(obj_it) == True:
                super(ContactList, self).remove(obj_it)
                self.maxid -= 1
                print("\nLe contact a été effacé !")
            self.flattendIds()
        [confirmation(obj_it) for obj_it in self if \
        getattr(obj_it, field) == value]
