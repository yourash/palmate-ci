import sys
from flask import Flask, got_request_exception
from flask_restful import Api

import executor.Leaves as Leaves
import executor.Projects as Projects
import executor.Builds as Builds
import executor.Config as Config

from common.Project import ProjectConfig
from common.Leaf import LeafConfig

# TODO(yourash): implement colored mitli-level logging
def logException(sender, exception, **extra):
    print('Exception occured: %s' % exception)

if len(sys.argv) != 3:
    print("Usage: %s host port" % sys.argv[0])
    sys.exit(0)

Config.checkDirs()

Builds.storage = Builds.BuildDAO(None)

for project in Config.getProjects():
    Projects.storage.addProject(ProjectConfig(project))

for leaf in Config.getLeaves():
    Leaves.storage.addLeaf(LeafConfig(leaf))


executorService = Flask("Executor")
executorService.config['BUNDLE_ERRORS'] = True
got_request_exception.connect(logException, executorService)

executorApi = Api(executorService)

executorApi.add_resource(Leaves.LeafIndex, '/leaves/')
executorApi.add_resource(Leaves.LeafResource, '/leaves/<int:leafId>')

executorApi.add_resource(Projects.ProjectIndex, '/projects/')
executorApi.add_resource(Projects.ProjectResource, '/projects/<int:projectId>')

executorApi.add_resource(Builds.BuildIndex, '/builds/')
executorApi.add_resource(Builds.BuildRecentIndex, '/builds/recent/')
executorApi.add_resource(Builds.BuildResource, '/builds/<int:buildId>')

executorService.run(host=sys.argv[1], port=sys.argv[2])

