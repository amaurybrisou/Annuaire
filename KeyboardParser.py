#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import Helps
import Utils
import os
import pickle


class KeyboardParser:
 
   
    def __init__(self, contacts, config, class_type):
        self.contacts = contacts
        self.config = config
        self.class_type = class_type
        FILENAME = config.get("MAIN", "FILENAME")
        self.parseMainArgs()

    def parseMainArgs(self):
        answer = ''
        while answer != "Q" :    
            Helps.my_help()
            answer = input("Votre choix : ")
            if answer == "S":
                try:
                    pickle.dump( self.contacts, open(self.config.get("MAIN", "filename"), "wb"))
                    Utils.setCurrentType(type(self.contacts), self.config)
                except IOError:
                    print("Error d\'écriture : vérifiez le permissions du système de fichier")                
                print("Vos contacts ont été sauvegardés correctement !")
            elif answer == "A":
                firstname = ''
                while Utils.sanitizeStrings(firstname) == False:
                    firstname = input("Veuillez indiquer un prénom : ")
                lastname = ''
                while Utils.sanitizeStrings(lastname) == False:
                    lastname = input("Veuillez indiquer le nom de famille : ")
                phone_number = ''
                while Utils.sanitizePhoneNumber(phone_number) == False:
                    phone_number = input("Veuillez indiquer le numéro de téléphone : ")
                self.contacts.append(firstname, lastname, phone_number)
            elif answer == "L":
                os.system('clear')
                if len(self.contacts) == 0:
                    print("vous n'avez aucun contact")
                    continue
                print("\n")
                print(self.contacts, sep="\n")
            elif answer == "H":
                os.system("clear")
            elif answer == "C":
                try:
                    self.contacts = pickle.load(open(self.config.get("MAIN", "FILENAME"), "rb"))
                except IOError:
                    print("Aucun Fichier")
            elif answer == "R":
                if len(self.contacts) == 0 :
                    print("vous n'avez aucun contact")
                    continue
                print("\n",self.parseSearchArgs())
            elif answer == "D":
                if len(self.contacts) == 0:
                    print("vous n'avez aucun contact")
                    continue
                self.parseDeleteArgs()
            elif answer == "M" :
                if len(self.contacts) == 0:
                    print("vous n'avez aucun contact")
                    continue
                obj = self.parseSearchArgs()
                if obj == None :
                    print("Ce contact n'existe pas !")
                    continue
                print("\n",obj)
                self.parseModArgs(obj)
        return
    
    
    def parseModArgs(self, obj):
        mod_field = ''
        value = ''
        while mod_field != "Q" :
            value = ''
            Helps.my_mod_help()
            mod_field = input("Votre choix : ")
            if mod_field == "P":
                value = "firstname"
            elif mod_field == "N":
                value = "lastname"
            elif mod_field == "T":
                value = "phone_number"
            self.contacts.modify(obj, value)

        
            

    def parseSearchArgs(self):
        search_methode = ''
        while search_methode != "Q":
            Helps.my_search_help()
            search_methode = input("Votre choix : ")
            if search_methode == "P":
                value = input("Prénom à rechercher : ").capitalize()
                field = "firstname"
                return self.contacts.index(field, value)
            elif search_methode == "N":
                value = input("Nom de famille à rechercher : ").capitalize()
                field = "lastname"
                return self.contacts.index(field, value)
            elif search_methode == "T":
                value = input("Numéro de téléphone à rechercher : ").capitalize()
                field = "phone_number"
                return self.contacts.index(field, value)
                    
                    
    def parseDeleteArgs(self):
        delete_methode = ''
        while delete_methode != "Q":
            Helps.my_delete_help()
            delete_methode = input("Votre choix : ")
            if delete_methode == "P":
                value = input("Prénom à Supprimer : ").capitalize()
                field = "firstname"
                self.contacts.remove(field, value)
            elif delete_methode == "N":
                value = input("Nom de famille à Supprimer : ").capitalize()
                field = "lastname"
                self.contacts.remove(field, value)
            elif delete_methode == "T":
                value = input("Numéro de téléphone à Supprimer : ").capitalize()
                field = "phone_number"
                self.contacts.remove(field, value)
