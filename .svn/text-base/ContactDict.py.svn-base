#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import Utils
from Contact import Contact
from ContactStdList import ContactStd


class ContactList(ContactStd, dict):

    def __init__(self, config):
        super().__init__(config)
        self.maxid = len(self)

    def append(self, firstname, lastname, phone_number):
        self[self.maxid] = Contact(firstname, lastname, phone_number)
        self.maxid += 1

    def __str__(self):
        ret = ""
        for obj in self:
            ret += str(self[obj])
        return ret

    def index(self, field, value):
        for m in [obj_it for obj_it in self if \
        getattr(self[obj_it], field) == value.capitalize()]:
            return self[m]

    def modify(self, obj, field):
        value = Utils.getNewValue(field)
        [setattr(self[obj_it], field, value) for obj_it in self if \
        self[obj_it] == obj and \
        (field == "firstname" or "lastname" or "phone_number" and value != "")]

    def remove(self, field, value):
        os.system('clear')

        def confirmation(obj_it):
            obj_it = obj_it[0]
            if self[obj_it] != None and Utils.AskForDeletion(obj_it) == True:
                del self[obj_it]
                self.maxid -= 1
                print("\nLe contact a été effacé !")
        del_dic = [obj_it for obj_it in self if \
        getattr(self[obj_it], field) == value]
        confirmation(del_dic)
