# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('dids'),XML('&trade;&nbsp;'),
                  _class="brand",_href=URL('default','index'))
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Cole Varner <colevarn@gmail.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = []

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    # useful links to internal and external resources
    response.menu += [
        (SPAN('dev'), False, '', [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, URL('admin', 'default', 'design/%s' % app)),
        (T('Database'), False, URL(app, 'appadmin', 'index'))
        ])]

if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
