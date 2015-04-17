import json
import random
import urllib2

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib2.Request(url=url, data=json.dumps(data), headers={
        "Content-Type":"application/json",
    })
    reply = json.load(urllib2.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

HOST="172.27.0.23"
PORT=8069
DB="odoodebugdb"
USER="admin"
PASS="password"
# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

print "uid is ", uid

# create a new idea
args = {
    'name' : 'Another idea',
    'description' : 'This is another idea of mine',
    'inventor_id': uid,
}
idea_id = call(url, "object", "execute", DB, uid, PASS, 'idea.idea', 'create', args)

print "idea_id is ", idea_id
