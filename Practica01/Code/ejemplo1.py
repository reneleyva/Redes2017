
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt

nombre = 'sin Nombre' 
""" 
   Clase que contiene un nombre como atributo 
"""
class Persona:
     def __init__(self, nombre_at = None):
        if nombre_at:
           self.nombre = nombre_at
        else:
           global nombre 
           self.nombre = nombre
""" 
   Clase que hereda de persona y agrega widgets 
   a sus atributos 
"""
class PersonaConWidgets(Persona):
     def __init__(self, nombre_at = "Sin Nombre", widgets = None):
        Persona.__init__(self, nombre_at)
        self.widgets = widgets if widgets else []

     def agrega_widget(self, nuevoWidget):
        self.widgets.append(nuevoWidget)
if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "l", ["local="])
    ejercicio = args[0]
    if(ejercicio == 'inicio'):
       persona_uno = Persona()
       print persona_uno.nombre
    if(ejercicio == 'atributos'):
       persona_uno = Persona()
       persona_dos = Persona('Juan')
       print persona_uno.nombre
       print persona_dos.nombre
       persona_dos.apellido = 'Lopez'
       print persona_dos.apellido
       print "Atributos de primera persona %s" %(persona_uno.__dict__)
       print "Atributos de segunda persona %s" %(persona_dos.__dict__)
    if ejercicio == 'herencia':
       widgets = ['Computadora']
       persona_derechos = PersonaConWidgets(widgets = widgets)
       persona_derechos.agrega_widget('Tablet')
       print persona_derechos.widgets