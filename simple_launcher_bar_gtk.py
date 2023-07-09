import sys
import gi
import os

from simple_launcher_bar_gtk_config import *

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Adw,Gio

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if side == Sides.LEFT or side == Sides.RIGHT:
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        elif side == Sides.DOWN or side == Sides.TOP:
            self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.set_child(self.box)

        self.buttons = []

        for l in launchers:
            button = Gtk.Button(label="Hello")
            
            self.box.append(button)
            
            button.set_icon_name(l.icon)

            button.set_size_request(size, size)
            

            self.buttons.append(button)

        
        


        # Things will go here

class LauncherBar(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = LauncherBar()
exit_status = app.run(sys.argv)
sys.exit(exit_status)