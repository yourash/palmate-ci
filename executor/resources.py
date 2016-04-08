from flask_restful import Resource, reqparse

class ProjectList(Resource):
    def get(self):
        return {'list of':'projects', 'in format':'TDB'}

class Project(Resource):
    def get(self, projectId):
        return {'project':projectId}

class ProjectBuilds(Resource):
    def get(self, projectId):
        return {'List of builds for':projectId}

class JobList(Resource):
    def get(self):
        return {'list of': 'jobs'}

class Job(Resource):
    def get(self, jobId):
        return { 'job':jobId}

class Build(Resource):
    def post(self, action):
        argParser = reqparse.RequestParser()
        argParser.add_argument('projectId',
                          dest='projectId',
                          required=True)
        args = argParser.parse_args()
        return {'projectId':args.projectId}
