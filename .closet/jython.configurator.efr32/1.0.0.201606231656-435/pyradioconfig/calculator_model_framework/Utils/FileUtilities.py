import os


class FileUtilities(object):

    #
    # delete the output directory and recreate it.  Start with an empty
    # directory for output files
    #
    @staticmethod
    def cleandir(dir):
        if os.path.exists(dir)== True:
            filelist = os.listdir(dir)
            for file in filelist:
                os.remove(dir + "/" + file)
        else:
            os.mkdir(dir)

    @staticmethod
    def printRootStructure(dirname,indent=0):
        print dirname
        for i in range(indent):
            print "   ",
        print os.path.basename(dirname) # changed
        if os.path.isdir(dirname):
            for files in os.listdir(dirname):
                FileUtilities.printRootStructure(os.path.join(dirname,files),indent+1) # changed


    @staticmethod
    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )