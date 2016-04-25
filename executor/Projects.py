from flask_restful import Resource

class ProjectStorage:
    def __init__(self, projects):
        self.__projects = dict()
        self.__currentId = 1

        for p in projects:
            self.addProject(p)

    def addProject(self, project):
        if self.checkProject(project):
            self.__projects[self.__currentId] = project
            self.__currentId += 1

    def removeProject(self, projectId):
        p = self.__projects.get(projectId)
        if p is not None:
            del self._projects[projectId]

    def numProjects(self):
        return len(self.__projects)

    def getProjectIds(self):
        return self.__projects.keys()

    def getProject(self, projectId):
        return self.__projects.get(projectId)

    def checkProject(self, project):
        for pId, p in self.__projects.items():
            if p.config['name'] == project.config['name']:
                print("Error: can't add two projects with identical names %s" % p.config.name)
                return False
        return True

storage = ProjectStorage([])

class ProjectIndex(Resource):
    def get(self):
        projects = list()
        for id in storage.getProjectIds():
            project = storage.getProject(id)
            print(project.config['name'])
            projects.append({project.config['name']: id})
        return {"projects":projects}

class ProjectResource(Resource):
    def get(self, projectId):
        project = storage.getProject(projectId)
        if project is None:
            return {"error": "Project with id %d does not exist"%projectId}, 404
        else:
            return project.config

