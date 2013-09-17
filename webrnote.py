#!/usr/bin/env python

import ctypes

import gi
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit, Soup



webView = WebKit.WebView()
webView.open('https://www.evernote.com/Home.action')
window = Gtk.Window()

icon_theme=Gtk.IconTheme.get_default()
if icon_theme.load_icon("evernote", 96, 0) : window.set_icon(icon_theme.load_icon("evernote", 96, 0))

window.set_size_request(1000,600)
window.set_title('Webrnote - Simple WebView Client for Evernote')

window.connect("delete-event", Gtk.main_quit)

s = Gtk.ScrolledWindow()

s.add(webView)
window.add(s)

cookiejar = Soup.CookieJarText.new("cookies/cookies.wbr", False)
cookiejar.set_accept_policy(Soup.CookieJarAcceptPolicy.ALWAYS)
session = WebKit.get_default_session()
session.add_feature(cookiejar)

window.show_all()
Gtk.main();
