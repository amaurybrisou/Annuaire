#! /usr/bin/env python3
#-*- coding:utf-8 -*-


class Contact(object):

    def __init__(self, *argv, **kargv):
            if len(argv) == 3:
                self.firstname = argv[0].capitalize().strip()
                self.lastname = argv[1].capitalize().strip()
                self.phone_number = argv[2].strip()
            else:
                self.maxid = argv[0]
                self.firstname = argv[1].capitalize().strip()
                self.lastname = argv[2].capitalize().strip()
                self.phone_number = argv[3].strip()

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + \
        self.phone_number + "\n"

    def __getstate__(self):
        contact_attr = self.__dict__.copy()
        return contact_attr

    def __setstate__(self, state):
        self.__dict__ = state
