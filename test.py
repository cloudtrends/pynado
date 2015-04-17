

url = 'http://172.27.0.23:8069'
db = 'odoodebugdb' 
username = 'admin'
password = 'password'

import xmlrpclib

url_str="https://demo.odoo.com/start"
url_str="http://172.27.0.23:8069/start"

if False:
    info = xmlrpclib.ServerProxy(url_str).start()
    url, db, username, password = \
    	info['host'], info['database'], info['user'], info['password']


print "url", url
print "database", db
print "username", username
print "password", password
#common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common = xmlrpclib.ServerProxy('{}/xmlrpc/common'.format(url))
print common.version()

uid = common.authenticate(db, username, password, {})
print "uid", uid
