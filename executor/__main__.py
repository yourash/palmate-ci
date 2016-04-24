import sys
from flask import Flask
from flask_restful import Api

import executor.Leaves as Leaves
import executor.Projects as Projects
import executor.Builds as Builds

if len(sys.argv) != 3:
    print("Usage: %s host port" % sys.argv[0])
    sys.exit(0)

executorService = Flask("Executor")

Leaves.storage.addLeaf({"host":"123456", "port":"12345"})

executorApi = Api(executorService)

executorApi.add_resource(Leaves.LeafIndex, '/leaves/')
executorApi.add_resource(Leaves.LeafResource, '/leaves/<int:leafId>')

executorApi.add_resource(Projects.ProjectIndex, '/projects')
executorApi.add_resource(Projects.ProjectResource, '/projects/<int:projectId>')

executorApi.add_resource(Builds.Build, '/builds/<int:projectId>')
executorService.run(host=sys.argv[1], port=sys.argv[2])

