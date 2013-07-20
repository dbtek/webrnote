#!/usr/bin/env python

import gtk
import webkit
import ctypes



libsoup = ctypes.CDLL('/usr/lib/i386-linux-gnu/libsoup-gnome-2.4.so.1')
libwebkit = ctypes.CDLL('/usr/lib/libwebkitgtk-1.0.so.0')


webView = webkit.WebView()
webView.open('https://www.evernote.com/Home.action')
window = gtk.Window()

window.resize(400,500)
window.set_icon_from_file('lib/icon.png')
window.set_size_request(1000,600)
window.set_title('Webrnote - Simple WebView Client for Evernote')

window.connect("destroy",window.destroy)
window.connect("delete_event", lambda w,e: gtk.main_quit())

s = gtk.ScrolledWindow()

s.add(webView)
window.add(s)

session = libwebkit.webkit_get_default_session()
cookiejar = libsoup.soup_cookie_jar_text_new('cookies/cookies.txt',False)
libsoup.soup_session_add_feature(session, cookiejar)

window.show_all()
gtk.mainloop()
