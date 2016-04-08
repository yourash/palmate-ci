#! /usr/bin/env python

import sys
from flask import Flask
from flask_restful import Api
import resources

executorService = Flask("Executor")
executorApi = Api(executorService)

executorApi.add_resource(resources.ProjectList, '/projects')
execturorApi.add_resource(resources.Project, '/projects/<int:projectId>')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s port" % sys.argv[0]
        sys.exit(0)
    executorApp.run(host='0.0.0.0', port=sys.argv[1])

