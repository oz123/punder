#!/usr/bin/env python

"""
punder - part two, populating a table with child widgets
UI is almost ready, tree view for track list is populated.
"""

import gtk

class PrefDialog():
    """
    create the preferences dialog
    """ 
    def set_encode(self):
        """
        add widgets to the page encoding
        """
        pg = self.notebook.get_nth_page(2)
        pg.set_border_width(5)
        alignment = gtk.Alignment(0, 0)
        vbox_inside = gtk.VBox(False, 0)
        vbox_inside.set_border_width(5)
        vbox_inside.pack_start(alignment)
        
        ogg_hbox = gtk.HBox(False,0)
        qLabel = gtk.Label("Quality")
        qLabel.set_alignment(5,0)

        ogg_frame = gtk.Frame()
        mp3_frame = gtk.Frame()
        flac_frame = gtk.Frame()
        
        #MP3
        mp3 = gtk.CheckButton(label="MP3 (lossy compression)" )
        mp3_frame.set_label_widget(mp3)
        mp3_hbox = gtk.HBox(False,0)
        bitrate_Label = gtk.Label("Bitrate")
        bitrate_Label.set_alignment(5,0)
        adj_mp3 = gtk.Adjustment(0, 0, 14, 1, 1, 1)
        scroll_mp3 = gtk.HScale(adj_mp3)
        scroll_mp3.set_digits(0)
        
        scroll_mp3.set_value_pos(gtk.POS_RIGHT)
        mp3_hbox.pack_start(bitrate_Label, False, False, 5)
        mp3_hbox.pack_start(scroll_mp3, True, True, 5)
        vboxmp3 = gtk.VBox()
        vboxmp3.pack_start(mp3_hbox)
        mp3_frame.add(vboxmp3)
        
        #OGG
        ogg = gtk.CheckButton(label="OGG Vorbis  (lossy compression)" )
        ogg_frame.set_label_widget(ogg)
      
        vboxogg = gtk.VBox()
        ogg_frame.add(ogg_hbox)
        adj_ogg = gtk.Adjustment(0.0, 0.0, 11.0, 0.1, 1.0, 1.0)
        ogg_scale = gtk.HScale(adj_ogg)
        ogg_scale.set_value_pos(gtk.POS_RIGHT)
        ogg_scale.set_digits(0)
        ogg_scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
        ogg_scale.set_draw_value(True)
        ogg_hbox.pack_start(qLabel, False, False, 5)
        ogg_hbox.pack_start(ogg_scale, True, True, 5)
        
        
        # FLAC
        flac = gtk.CheckButton(label="FLAC (lossless compression)" )
        flac_frame.set_label_widget(flac)
        flac_hbox = gtk.HBox(False,0)
        compression_Label = gtk.Label("Compression level")
        compression_Label.set_alignment(5,0)
        
        adj_flac = gtk.Adjustment(0.0, 0.0, 9.0, 0.1, 1.0, 1.0)
        scroll_flac = gtk.HScale(adj_flac)
        scroll_flac.set_value_pos(gtk.POS_RIGHT)
        scroll_flac.set_digits(0)
        flac_hbox.pack_start(compression_Label, False, False, 5)
        flac_hbox.pack_start(scroll_flac, True, True, 5)
        vboxflac = gtk.VBox()
        vboxflac.pack_start(flac_hbox)
        flac_frame.add(vboxflac)
        
        # Other formats
        expander = gtk.Expander(label="More formats")

        # WAV PACK
        wv_pk_frame = gtk.Frame()
        hybrid_frame = gtk.Frame()        
        wv_pk = gtk.CheckButton(label="WavPack" )
        wv_pk_frame.set_label_widget(wv_pk)
        wvpk_hbox = gtk.HBox(False,0)
        compression_wv_pk = gtk.Label("Compression level")
        compression_wv_pk.set_alignment(5,0)
        
        adj_wv_pk = gtk.Adjustment(0.0, 0.0, 9.0, 0.1, 1.0, 1.0)
        scroll_wv_pk = gtk.HScale(adj_wv_pk)
        scroll_wv_pk.set_value_pos(gtk.POS_RIGHT)
        scroll_wv_pk.set_digits(0)
        wvpk_hbox.pack_start(compression_wv_pk, False, False, 5)
        wvpk_hbox.pack_start(scroll_wv_pk, True, True, 5)
        
        vbox_wv_pk = gtk.VBox()
        vbox_wv_pk.pack_start(wvpk_hbox)
        wv_pk_frame.add(vbox_wv_pk)
        
        hybrid_button = gtk.CheckButton(label="Hybrid Compression")
        hybrid_frame.set_label_widget(hybrid_button)
        hybrid_alignment = gtk.Alignment(0.5, 0.5, 1, 1)
        hybrid_alignment.add(hybrid_frame)
        hybrid_alignment.set_padding(2, 2, 12, 2)
        adj_hybrid = gtk.Adjustment(0.0, 0.0, 9.0, 0.1, 1.0, 1.0)
        scroll_hybrid = gtk.HScale(adj_hybrid)
        scroll_hybrid.set_value_pos(gtk.POS_RIGHT)
        scroll_hybrid.set_digits(0)
        
        hybrid_hbox = gtk.HBox(False,0)
        bitrate_hybrid_label = gtk.Label("Bitrate")
        bitrate_hybrid_label.set_alignment(5,0)
        
        hybrid_hbox.pack_start(bitrate_hybrid_label, False, False, 5)
        hybrid_hbox.pack_start(scroll_hybrid)

        hybrid_frame.add(hybrid_hbox)
        vbox_wv_pk.pack_start(hybrid_alignment,True, True, 5)
        
        # MUSEPACK
        musepk_frame = gtk.Frame()
        musepk_button = gtk.CheckButton(label="Musepack (lossy compression)" )
        musepk_frame.set_label_widget(flac)
        musepk_hbox = gtk.HBox(False,0)
        musepk_compression_Label = gtk.Label("Compression level")
        musepk_compression_Label.set_alignment(5,0)
        adj_musepk = gtk.Adjustment(0.0, 0.0, 6.0, 0.1, 1.0, 1.0)
        scroll_musepk = gtk.HScale(adj_musepk)
        scroll_musepk.set_value_pos(gtk.POS_RIGHT)
        scroll_musepk.set_digits(0)
        musepk_hbox.pack_start(musepk_compression_Label, False, False, 5)
        musepk_hbox.pack_start(scroll_flac, True, True, 5)
        vboxmusepk = gtk.VBox()
        vboxmusepk.pack_start(musepk_hbox)
        musepk_frame.add(vboxmusepk)
        
        # add frames to expander
        expander.add(wv_pk_frame)
        expander.add(musepk_frame)
        
        # WAV
        wv_bttn = gtk.CheckButton(label="WAV (Uncompressed)")
        
        pg.pack_start(wv_bttn, False, False, 0)
        pg.pack_start(mp3_frame, False, False, 0)
        pg.pack_start(ogg_frame, False, False, 0)
        pg.pack_start(flac_frame, False, False, 0)
        pg.pack_start(expander)
        
    def set_file_names(self):
        """
        add widgets to the page File Names
        """
        pg = self.notebook.get_nth_page(1)
        pg.set_border_width(5)
        alignment = gtk.Alignment(0, 0)
        frame = gtk.Frame("Filename format")
        text_formaters = gtk.Label("%A - Artist\n%L - Album\n%N - Track number " \
        + "(2-digit)\n%Y - Year (4-digit or \"0\")\n%T - Song title\n" \
        + "%G - Genre")
        
        alignment.add(text_formaters)
        vbox_inside = gtk.VBox(False, 0)
        vbox_inside.set_border_width(5)
        vbox_inside.pack_start(alignment)
        
        frame.add(vbox_inside)

        # add table to populate more widgets
        filenames_table = gtk.Table(3, 2, False)
        vbox_inside.pack_start(filenames_table,  True, True, 0)
        
        album_dir = gtk.Label("Album directory: ")
        album_dir.set_alignment(0, 0.5)
        playlist_file = gtk.Label("Playlist file: ")
        playlist_file.set_alignment(0, 0.5)
        music_file = gtk.Label("Music file: ")
        music_file.set_alignment(0, 0.5)
        
        album_entry = gtk.Entry(128)
        # dummy entries, should be later read from the config file
        album_entry.set_text("%A - %L")
        album_entry.set_tooltip_text("This is relative to the destination folder (from the General tab).\n"
                                                        "Can be blank.\n"
                                                        "Default: %A - %L\n"
                                                        "Other example: %A/%L")        
        playlist_entry = gtk.Entry(128)
        # dummy entries, should be later read from the config file
        playlist_entry.set_text("%A - %L")
        playlist_entry.set_tooltip_text("This will be stored in the album directory.\n"
                                                        "Can be blank.\n"
                                                        "Default: %A - %L")
        musicfile_entry = gtk.Entry(128)
        # dummy entries, should be later read from the config file
        musicfile_entry.set_text("%N - %A - %T")
        musicfile_entry.set_tooltip_text("This will be stored in the album directory.\n"
                                                     "Cannot be blank.\n"
                                                     "Default: %A - %T\n"
                                                     "Other example: %N - %T")
        
        # album_table.attach(child, left, right, top, bottom)
        filenames_table.attach(album_dir, 0, 1, 0, 1,  gtk.FILL)
        filenames_table.attach(playlist_file, 0, 1, 1, 2,  gtk.FILL)
        filenames_table.attach(music_file, 0, 1, 2, 3,  gtk.FILL)
        
        filenames_table.attach(album_entry, 1, 2, 0, 1, gtk.FILL)
        filenames_table.attach(playlist_entry, 1, 2, 1, 2,  gtk.FILL|gtk.EXPAND)
        filenames_table.attach(musicfile_entry, 1, 2, 2, 3,gtk.FILL)
        

        pg.pack_start(frame, False, False, 0)
        
    def set_general_page(self):
        """
        add widgets to the page General
        """    
        # populate general tab with proper stuff
        generalpage = self.notebook.get_nth_page(0)
        alignment = gtk.Alignment(0,0)
        filechooserlabel = gtk.Label("Destination folder")
        #filechooserlabel.set_justify(gtk.JUSTIFY_LEFT)
        alignment.add(filechooserlabel)
        filechooserbutton = gtk.FileChooserButton("Destination folder")
        filechooserbutton.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        generalpage.pack_start(alignment, False, False, 0)
        generalpage.pack_start(filechooserbutton,  False, False, 0)
        
        #generalpage.add(generalvbox)
        
        # add check button for making m3u playlist
        make_playlist = gtk.CheckButton("Create M3U playlist")
        # make default as true
        make_playlist.set_active(True)
        generalpage.pack_start(make_playlist,  False, False, 0)
        
        # add the cdrom drive entry inside an hbox
        hbox = gtk.HBox(False)
        cdrom_label = gtk.Label("CD-ROM device: ")
        cdrom = gtk.Entry(128)
        cdrom.set_text("/dev/sr0")
        cdrom.set_tooltip_text("Default: /dev/cdrom\n"
                               "Other example: /dev/hdc\n"
                               "Other example: /dev/sr0")
        hbox.pack_start(cdrom_label, False, False, 0)
        hbox.pack_start(cdrom, False, False, 0)
        generalpage.pack_start(hbox, False,False, 0)
        
        eject_cd = gtk.CheckButton("Eject disc when finished")
        generalpage.pack_start(eject_cd, False,False, 0)
        
    def insert_notebook(self):
        """
        create a notebook with 4 pages, each containing a gtk.VBox.
        """
        self.notebook = gtk.Notebook()
        
        for idx, page in enumerate(["General", "File Names", "Encode", 
            "Advanced"]):
            # later, we can replace widget with a vbox, and then
            # the road is wide open to start packing other widgets inside it!
            vbox = gtk.VBox(False)
            self.notebook.append_page(vbox)
            # note: you could also do
            # label = gtk.Label(page)
            # self.notebook.append_page(vbox, tab_label = label)
            pg = self.notebook.get_nth_page(idx)
            self.notebook.set_tab_label_text(pg, page)
        
        self.set_general_page()
        self.set_file_names()
        self.set_encode()
        self.dialog.vbox.pack_start(self.notebook)
   
    
    def __init__(self, window):
        """
        initialize the preferences dialog
        """
        # title, parent, flags (0, for defaults), no buttons
        self.dialog = gtk.Dialog("Preferences", window, 0,
        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))

        self.dialog.set_default_size(250, 300)
        
        #self.insert_label()
        self.insert_notebook()
        response = self.dialog.show_all()
        response = self.dialog.run()
        

        
        if response == gtk.RESPONSE_OK:
            print "The OK button was clicked"
        elif response == gtk.RESPONSE_CANCEL:
            print "The Cancel button was clicked"
        
        self.dialog.destroy()

        

class PunderUI():
    """
    Initial class to draw the first toolbar.
    """
    def pref_dialog(self, widget):
        """
        A simple method to initiate a PrefDialog instance.
        """
        PrefDialog(self.window)
    
    def help_dialog(self, widget):
        """
        create a GTK help dialog upon button click and destroy it when pressing the
        close button
        """
        self.about = gtk.AboutDialog()
        sometext=gtk.Label('This is just the beggining.\nWill Get back to it  later.')
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
        
        column_titles = ["Track", "Artist", "Title", "Duration"]
        for idx, title in enumerate(column_titles):
            rendererText = gtk.CellRendererText()
            column = gtk.TreeViewColumn(title, rendererText, text=idx)
            column.set_sort_column_id(idx)
            treeView.append_column(column)


    def __init__(self):
        """
        create the gui using GTK Window, and Toolbar.
        """
        self.window = gtk.Window()
        self.window.set_default_size(500, -1)

        # Set VBox to heterogeneous so different widgets can have 
        # different sizes 
        # All widgets attached will be the same size
        # Setting homogeneous to false makes the UI look sane
        # only in a few cases we create VBOX with the homogenous option
        vbox = gtk.VBox(False)
        self.window.add(vbox)

       
        toolbar = gtk.Toolbar()
        
        button1 = gtk.ToolButton()
        button1 = gtk.ToolButton(gtk.STOCK_REFRESH)
        
        button1.set_label("CDDB")
        button1.set_is_important(True)
        
        # Add preferences button 
        pref_button = gtk.ToolButton(gtk.STOCK_PREFERENCES)
        # Setting the button to important, shows its label
        pref_button.set_is_important(True)
        # connect the button the pref_dialog method
        pref_button.connect("clicked", self.pref_dialog)
        
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
        button_about.set_is_important(True)
        
        # with .connect we make a button do something
        # in this case, the event clicked will trigger
        # the class method rundialog
        # gtk.Button is inherited from the class gobject
        # hence it contains also the method connect, which
        # takes by default 2 arguments:
        # def connect(detailed_signal, handler, ...)
        # see more info the [method documentation][doc1]
        button_about.connect("clicked", self.help_dialog)
        
        self.window.connect("destroy", lambda w: gtk.main_quit())
        # we don't use window.add anymore, instead we use pack!
        toolbar.insert(button1, 0)
        toolbar.insert(pref_button, 1)
        toolbar.insert(separator1, 2)
        toolbar.insert(button_about, 3)
        vbox.pack_start(toolbar, False)
        
        # a table is a very convient way to populate the window
        # with many different elements. A table can be packed too!
        
        album_table = gtk.Table(3, 3, False)
        # set fill to False so when resizing the window, it does not 
        # expand !
        vbox.pack_start(album_table, False)
        
        artist_name = gtk.Entry(128)
        artist_name.set_text("Unknown Artist")
        artist_label = gtk.Label('Album Artist:')
        artist_label.set_alignment(0, 0.5)
        # child widgets are connected to the table with the method
        # attach.
        # album_table.attach(child, left, right, top, bottom)
        # the coordinates start from 0, 0 at the top left corner of
        # the table
        album_table.attach(artist_label, 0, 1, 0, 1,  gtk.FILL)
        album_table.attach(artist_name, 1, 2, 0, 1, gtk.EXPAND | gtk.FILL)
 
        album_name = gtk.Entry(128)
        album_name.set_text("Unknown Album")
        album_label = gtk.Label('Album Title:')
        album_label.set_alignment(0, 0.5)
        
        album_table.attach(album_label, 0, 1, 1, 2, gtk.FILL)
        album_table.attach(album_name, 1, 2, 1, 2, gtk.EXPAND | gtk.FILL)

        album_year = gtk.Entry(4)
        album_year.set_text("1900")
        album_genre = gtk.Entry(128)
        album_genre.set_text("Unknown")

        album_genyear = gtk.Label('Genre / Year:')
        album_genyear.set_alignment(0,0.5)

        album_table.attach(album_genyear, 0, 1, 2, 3, gtk.FILL)
        album_table.attach(album_year, 2, 3, 2, 3, gtk.FILL)
        album_table.attach(album_genre, 1, 2, 2, 3, gtk.EXPAND | gtk.FILL)
        
        
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
        album_table.attach(single_artist, 2, 3, 0, 1,gtk.FILL)
        
        treeview.set_rules_hint(True)
        vbox.pack_start(treeview)
        self.window.show_all()



        
PunderUI()
gtk.main()

# [doc1]: http://www.pygtk.org/docs/pygobject/class-gobject.html#method-gobject--connect 
