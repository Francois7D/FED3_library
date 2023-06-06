
sourcefolder = "C:\\Users\\François Ducroux\\Documents\\GitHub\\FED3_library\\src"
destfolder = "C:\\Users\\François Ducroux\\Documents\\Arduino\\libraries\\FED3\\src\\"

from distutils.dir_util import copy_tree
copy_tree(sourcefolder, destfolder)
