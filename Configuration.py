#!/usr/bin/env python
#-*- coding:utf-8 -*-

import configparser


class Configuration(configparser.ConfigParser):

    def __init__(self):
        super().__init__()
        self.config = self.read('example.cfg')
