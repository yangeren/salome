__author__ = 'Hanz'
from my_flask import app
from flask import current_app

print current_app.__name__
print '1'

app_ctx = app.app_context()
app_ctx.push()
print current_app.name
app_ctx.pop()
# print current_app.name

print app.url_map