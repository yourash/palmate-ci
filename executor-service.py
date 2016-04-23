#! /usr/bin/env python3

import sys
from flask import Flask
from flask_restful import Api

import executor.Nodes as Nodes
import executor.Projects as Projects
import executor.Builds as Builds

executorService = Flask("Executor")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s host port" % sys.argv[0])
        sys.exit(0)

    Nodes.nodeStorage.addNode({"host":"123456", "port":"12345"})

    executorApi = Api(executorService)

    executorApi.add_resource(Nodes.NodeList, '/nodes/')
    executorApi.add_resource(Nodes.Node, '/nodes/<int:nodeId>')

    executorApi.add_resource(Projects.ProjectList, '/projects')
    executorApi.add_resource(Projects.Project, '/projects/<int:projectId>')

    executorApi.add_resource(Builds.Build, '/builds/<int:projectId>')
    executorService.run(host=sys.argv[1], port=sys.argv[2])

