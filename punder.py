#!/usr/bin/env python

"""
punder - part one, making a button do something:

creating a very very basic UI. A tool bar with Four buttons. 
2 of the buttones contain icons and text, and two buttons contain
just icons.
"""

import gtk

class PySunder():
    """
    Initial class to draw the first toolbar.
    """
    def help_dialog(self, widget):
        """
        create a GTK help dialog upon button click and destroy it when pressing the 
        close button
        """
        self.about = gtk.AboutDialog()
        sometext=gtk.Label('This is just the beggining.\nWill Get back to later.')
        self.about.vbox.pack_start(sometext)      
        self.about.show_all()
        result = self.about.run() 
        # adding this will cause the about dialog to close when we
        # press the button 'Close'.
        self.about.hide()
    
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
        #button_help = gtk.ToolButton(gtk.STOCK_HELP)
        #button_help.set_is_important(True)
        button_about = gtk.ToolButton(gtk.STOCK_ABOUT)
        
        # if you set a button to not important, it's text label
        # will not be shown!
        # unlike button2.set_is_important(True)
        button_about.set_is_important(False)
        
        # with .connect we make a button do something
        # in this case, the event clicked will trigger
        # the class method rundialog
        # gtk.Button is inherited from the class gobject
        # hence it contains also the method connect, which
        # takes by default 2 arguments:
        # def connect(detailed_signal, handler, ...)
        # see more info the [method documentation][doc1]
        button_about.connect("clicked", self.help_dialog)
        
        window.connect("destroy", lambda w: gtk.main_quit())       
        window.add(toolbar)
        toolbar.insert(button1, 0)
        toolbar.insert(button2, 1)
        toolbar.insert(separator1, 2)
        toolbar.insert(button_about, 3)
        window.show_all()

PySunder()
gtk.main()

# [doc1]: http://www.pygtk.org/docs/pygobject/class-gobject.html#method-gobject--connect 
