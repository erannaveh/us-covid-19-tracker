##!/usr/bin/python3
import sys
import index
from app import app, server



debugMode = False
if (len(sys.argv) > 1):
    debugMode = (sys.argv[1] == 'debug')

@server.route('/')
def MyDashApp():
    app.title = 'US COVID-19 Tracker'
    return app.index()

print("Debug is ", debugMode)
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=debugMode)

