# -*- coding: utf-8 -*-

from main import Main 


def name():
    return "Transfer-Atributos"

def description():
    return "Transferi atributos de uma determinada feição para as demais selecionada"

def version():
    return "Version 0.1"

def classFactory(iface):
    return Main(iface)

def qgisMinimumVersion():
    return "2.0"

def author():
    return "jossan costa"

def email():
    return "me@hotmail.com"

def icon():
    return "icon.png"

