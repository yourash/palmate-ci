#! /usr/bin/env python

import sys
from flask import Flask
from flask_restful import Api
import resources

configuratorApp = Flask("Configurator")
configuratorApi = Api(configuratorApp)

configuratorApi.add_resource(resources.ProjectList, '/')
configuratorApi.add_resource(resources.Project, '/<int:projectId>')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s port" % sys.argv[0]
        sys.exit(0)
    configuratorApp.run(host='0.0.0.0', port=sys.argv[1])

