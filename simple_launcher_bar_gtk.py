import sys
import gi
import os

from simple_launcher_bar_gtk_config import *

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class LauncherBar(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name('My Gtk Application')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Hello World")
        window.present()


app = LauncherBar()
exit_status = app.run(sys.argv)
sys.exit(exit_status)