#! /usr/bin/env python

import sys
from flask import Flask
from flask_restful import Api

import Nodes
import Projects
import Builds

executorService = Flask("Executor")
executorApi = Api(executorService)

executorApi.add_resource(Nodes.NodeList, '/nodes/')
executorApi.add_resource(Nodes.Node, '/nodes/<int:nodeId>')

executorApi.add_resource(Projects.ProjectList, '/projects')
executorApi.add_resource(Projects.Project, '/projects/<int:projectId>')

executorApi.add_resource(Builds.Build, '/builds/<int:projectId>')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: %s host port" % sys.argv[0]
        sys.exit(0)
    executorService.run(host=sys.argv[1], port=sys.argv[2])

