#! /usr/bin/env python3B
#-*- coding:utf-8 -*-

import re, os

def getClass(annuaire_type):
    module = "Contact"+annuaire_type.capitalize()
    module = __import__( module )
    my_type = getattr( module, "ContactList")
    return my_type
    
def sanitizePhoneNumber(phone_number):
    ret = False
    res = re.match('^(0|\+33)[1-9]([-. ]?[0-9]{2}){4}$', phone_number)
    if res:
        ret = True
    return ret

def getNewValue(field):
    value = ''
    if field == "firstname":
        while sanitizeStrings(value) == False:
            value = input("\nNouveau prénom : ").capitalize()
    elif field == "lastname":
        while sanitizeStrings(value) == False:
            value = input("\nNouveau nom : ").capitalize()
    elif field == "phone_number":
        while sanitizePhoneNumber(value) == False:
            value = input("\nNouveau téléphone : ")
    return value

def AskForDeletion(obj_it):
    print("\nVoici le contact à supprimer :",obj_it)
    confirmation = "O"
    confirmation = input("Confirmez-vous la suppression de ce contact ? (O/n) ")
    if confirmation != "O":
        return False
    else:
        print(obj_it)
        return True
        
def sanitizeStrings(string):
    ret = False
    res = re.match('[^\W\d_]{2,}', string) # \w => Chiffres Lettres Caractères spéciaux
    if res:
        ret = True
    return ret

def sanitizeId(string):
    ret = False
    res = re.match('\d+', string)
    if res:
        ret = True
    return ret
    
def sanitizeInteger(input_int):
    ret = False
    res = re.match('\d{1}', input_int)
    if res:
        ret = True
    return ret

def setCurrentType(annuaire_type, config):
    config.set("MAIN", "old_type" ,str(annuaire_type))
    with open("example.cfg", 'w') as configfile:
        config.write(configfile)
        
def CheckOldFormat(config, contacts_type):
    old_type = config.get("MAIN", "old_type")
    if old_type != repr(contacts_type):
        print("Mauvais Format, format actuel : ",old_type," vous demandez le format : ",contacts_type)
        rep = ""
        while rep != "O":
            rep = input("Si vous continuez, l\'ancien Annuaire sera détruit, Voulez vous continuer (n/O) ?")
            if rep == "O":
               return True
            else:
                os._exit(1)
