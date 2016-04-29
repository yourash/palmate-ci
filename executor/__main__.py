import sys
from flask import Flask, got_request_exception
from flask_restful import Api
from pymongo import MongoClient

import executor.Leaves as Leaves
import executor.Projects as Projects
import executor.Builds as Builds
import executor.Config as Config

from common.Project import ProjectConfig
from common.Leaf import LeafConfig
from common import Logger

# TODO(yourash): implement colored mitli-level logging
def logException(sender, exception, **extra):
    print('Exception occured: %s' % exception)

class ExecutorApp:
    def __init__(self, host, port):
        self.logger = Logger.Logger('/var/palmate-executor.log')
        self.loadConfigs()
        self.host = host
        self.port = port

        self.service = Flask('Executor')
        self.service.config['BUNDLE_ERRORS'] = True
        got_request_exception.connect(logException, self.service)
        self.api = Api(self.service)

        self.api.add_resource(Leaves.LeafIndex, '/leaves/')
        self.api.add_resource(Leaves.LeafResource, '/leaves/<int:leafId>')

        self.api.add_resource(Projects.ProjectIndex, '/projects/')
        self.api.add_resource(Projects.ProjectResource, '/projects/<int:projectId>')

        self.api.add_resource(Builds.BuildIndex, '/builds/')
        self.api.add_resource(Builds.BuildRecentIndex, '/builds/recent/')
        self.api.add_resource(Builds.BuildResource, '/builds/<int:buildId>')

    def run(self):
        self.connectDb()
        self.initStorages()
        self.service.run(host=self.host, port=self.port)


    def loadConfigs(self):
        Config.checkDirs()
        # TODO: load Executor configuration from .palmate/executor.yaml
        self.mongoHost='localhost'
        self.mongoPort=27017

    def initStorages(self):
        for project in Config.getProjects():
            Projects.storage.addProject(ProjectConfig(project))

        for leaf in Config.getLeaves():
            Leaves.storage.addLeaf(LeafConfig(leaf))

        Builds.storage = Builds.BuildDAO(self.mongoClient['builds-db'])

    def connectDb(self):
        # TODO(yourash): implement colored mitli-level logging
        self.logger.info('Connecting to mongodb at %s:%d' % (self.mongoHost, self.mongoPort))
        self.mongoClient = MongoClient(self.mongoHost, self.mongoPort)
        serverInfo = self.mongoClient.server_info()
        self.logger.info('Connected, server info:')
        self.logger.info(serverInfo)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s host port" % sys.argv[0])
        sys.exit(0)

    if len(sys.argv) == 4:
        Config.__configBasePath = sys.argv[3]

    executor = ExecutorApp(sys.argv[1], sys.argv[2])
    executor.run()

