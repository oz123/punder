#!/usr/bin/env python

"""
punder - part one:

creating a very very basic UI. A tool bar with Four buttons. 
2 of the buttones contain icons and text, and two buttons contain
just icons.
"""

import gtk

class PySunder():
    """
    Initial class to draw the first toolbar.
    """
    def __init__(self):
        """
        create the gui using GTK Window, and Toolbar.
        """
        window = gtk.Window()
        window.set_default_size(500, -1)
        
        toolbar = gtk.Toolbar()
        # bad naming convention
        button1 = gtk.ToolButton()
        button1 = gtk.ToolButton(gtk.STOCK_REFRESH)
        
        button1.set_label("CDDB")
        button1.set_is_important(True)
        
        button2 = gtk.ToolButton(gtk.STOCK_PREFERENCES)
        button2.set_is_important(True)
        
        separator1 = gtk.SeparatorToolItem()
        
        # more verbose ... hard to type, but nothing that 
        # a decent IDE can not cope with. 
        # give your items clear name, which indicate
        # their roles
        button_help = gtk.ToolButton(gtk.STOCK_HELP)
        button_help.set_is_important(True)
        button_about = gtk.ToolButton(gtk.STOCK_ABOUT)
        button_about.set_is_important(False)
        
        window.connect("destroy", lambda w: gtk.main_quit())       
        window.add(toolbar)
        toolbar.insert(button1, 0)
        toolbar.insert(button2, 1)
        toolbar.insert(separator1, 2)
        toolbar.insert(button_help, 3)
        toolbar.insert(button_about,4)
        # launch the window.
        window.show_all()

PySunder()
gtk.main()
