import os, sys
import common.Project as Project

__configDir = os.path.expanduser('~')+'/.palmate/'
__configExtension = '.yml'
__configPaths = [
            __configDir+'projects/',
            __configDir+'leaves/'
        ]

def checkDirs():
    for path in __configPaths:
        if not os.path.exists(path):
            os.makedirs(path)

def getProjects():
    projectPath = __configDir+'/projects/'
    return [projectPath+f for f in os.listdir(projectPath)
            if os.path.isfile(os.path.join(projectPath, f)) and
            f.endswith(__configExtension)]

def getLeaves():
    leafPath = __configDir+'/leaves/'
    return [leafPath+f for f in os.listdir(leafPath)
            if os.path.isfile(os.path.join(leafPath, f)) and
            f.endswith(__configExtension)]

