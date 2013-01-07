#!/usr/bin/env python

"""
punder - part two, populating a table with child widgets
UI is almost ready, tree view for track list is populated.
"""

import gtk

class PunderUI():
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
    
    def on_toggle(self, cell, path, list_store):
        """
        a click event on the check button should negate
        the content of the button.
        """
        if path is not None:
            iterator = list_store.get_iter(path)
            list_store[iterator][0] = not list_store[iterator][0]
        
            
    def create_columns(self, treeView):
        """
        create columns for treeview of track list
        """
        cell = gtk.CellRendererToggle()
        cell.connect("toggled", self.on_toggle, self.liststore)
        column = gtk.TreeViewColumn("Rip",cell,active=0)
        column.set_sort_column_id(0)
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Track", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Artist", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Title", rendererText, text=3)
        column.set_sort_column_id(3)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Duration", rendererText, text=4)
        column.set_sort_column_id(4)
        treeView.append_column(column)

    def __init__(self):
        """
        create the gui using GTK Window, and Toolbar.
        """
        window = gtk.Window()
        window.set_default_size(500, -1)
        vbox = gtk.VBox()
        window.add(vbox)
       
        toolbar = gtk.Toolbar()
        
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
        # we don't use window.add anymore, instead we use pack!
        toolbar.insert(button1, 0)
        toolbar.insert(button2, 1)
        toolbar.insert(separator1, 2)
        toolbar.insert(button_about, 3)
        vbox.pack_start(toolbar, False)
        
        # a table is a very convient way to populate the window
        # with many different elements. A table can be packed too!
        album_table = gtk.Table(3, 3, False)
        vbox.pack_start(album_table)
        
        artist_name = gtk.Entry(128)
        artist_name.set_text("Unknown Artist")
        artist_label = gtk.Label('Album Artist:')
       
        # child widgets are connected to the table with the method
        # attach.
        # album_table.attach(child, left, right, top, bottom)
        # the coordinates start from 0, 0 at the top left corner of
        # the table
        album_table.attach(artist_label, 0, 1, 0, 1)
        album_table.attach(artist_name, 1, 2, 0, 1)
 
        album_name = gtk.Entry(128)
        album_name.set_text("Unknown Album")
        album_label = gtk.Label('Album Title:')
        
        album_table.attach(album_label, 0, 1, 1, 2)
        album_table.attach(album_name, 1, 2, 1, 2)
        
        album_year = gtk.Entry(4)
        album_year.set_text("1900")
        album_genre = gtk.Entry(128)
        album_genre.set_text("Unknown")
        album_genyear = gtk.Label('Genre/Year:')
        
        album_table.attach(album_year, 2, 3, 2, 3)
        album_table.attach(album_genre, 1, 2, 2, 3)
        album_table.attach(album_genyear, 0, 1, 2, 3)
        
        self.liststore = gtk.ListStore(bool,int,str,str,str)
        treeview = gtk.TreeView(self.liststore)
        # dummy function
        
        for i in range(1,6):
           tree_iter = self.liststore.append([True,i,"bar","baz","zap"])
        
        # access the table values as a coordinate system (like in gtk.Table)
        self.liststore[2][0] = False
        
        # or you can use the iterators approach
        path = self.liststore.get_path(tree_iter)
        self.ls_iter = self.liststore.get_iter_first()
        # liststore.set_value(iter, column, value)
        self.liststore.set_value(self.ls_iter, 3, "First Track")
        second = self.liststore.iter_next(self.ls_iter)
        third = self.liststore.iter_next(second)
        self.liststore.set_value(third, 2, "Famous Singer")

        #treeview = gtk.TreeView(store)
        treeview.set_rules_hint(True)
        treeview.set_enable_search(False)
        self.create_columns(treeview)
        
        # add a checkbox for marking Single Artist
        single_artist = gtk.CheckButton("Single Artist")
        album_table.attach(single_artist, 2, 3, 0, 1)
        
        treeview.set_rules_hint(True)
        vbox.pack_start(treeview)
        
        window.show_all()



        
PunderUI()
gtk.main()

# [doc1]: http://www.pygtk.org/docs/pygobject/class-gobject.html#method-gobject--connect 
