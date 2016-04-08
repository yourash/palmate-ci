#! /usr/bin/env python

import sys
from flask import Flask
from flask_restful import Api
import resources

executorService = Flask("Executor")
executorApi = Api(executorService)

executorApi.add_resource(resources.ProjectList, '/projects')
executorApi.add_resource(resources.Project, '/projects/<int:projectId>')
executorApi.add_resource(resources.ProjectBuilds, '/projects/<int:projectId>/builds')

executorApi.add_resource(resources.JobList, '/jobs')
executorApi.add_resource(resources.Job, '/jobs/<int:jobId>')

executorApi.add_resource(resources.Build, '/build/<string:action>')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: %s host port" % sys.argv[0]
        sys.exit(0)
    executorService.run(host=sys.argv[1], port=sys.argv[2])

