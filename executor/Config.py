import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import common.Project as Project
import hjson

def getProjects():
    projectpath = join(os.path.expanduser('~')+'/.sci/projects/'))
    return [f for f in os.listdir(projectpath) 
            if isfile(join(projectpath, f)) and f.endswith('hjson')]
