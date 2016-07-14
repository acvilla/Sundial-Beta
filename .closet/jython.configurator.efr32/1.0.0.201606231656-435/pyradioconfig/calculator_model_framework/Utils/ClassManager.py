import inspect
import md5
import os.path
import imp
import traceback
import sys
import time
import os

__all__ = ['ClassManager']

"""
Common utitly class
"""
class ClassManager(object):
    """
    Loads py file by path
    """
    @staticmethod
    def load_module(full_code_path):
        try:
            try:
                #code_dir = os.path.dirname(full_code_path)
                code_file = os.path.basename(full_code_path)
                code_file, ext = os.path.splitext(code_file)

                # Hack:  Can't use "." in class name,
                # so repalced with "_"
                class_name = full_code_path.replace(".", "_")
                class_name = class_name.replace("\\", "_")
                class_name = class_name.replace("/", "_")
                pos = class_name.rfind('.py')
                class_name = class_name[:pos] # remove .py extention
                pos = class_name.rfind(':_')
                class_name = class_name[pos+2:] # starting drive

                fin = open(full_code_path, 'rb')

                #return  imp.load_source(md5.new(full_code_path).hexdigest(), full_code_path, fin)
                name, ext = os.path.splitext(full_code_path)
                if ext.upper() == '.PY':
                    return  imp.load_source(class_name, full_code_path, fin)
                else:
                    return  imp.load_compiled(class_name, full_code_path + "c", fin)
            finally:
                try: fin.close()
                except: pass
        except ImportError, x:
            traceback.print_exc()
            raise
        except:
            traceback.print_exc()
            raise

    """
    Loads itertable classes file by path
    """
    @staticmethod
    def getClasses(path):
        try:
            #path = path + "0" # HACK!!!
            # Import profile modules and classes
            path = os.path.realpath(path)
            if  os.path.exists(path):
                foo = imp.load_source('__init__', path)
            else:
                path = path + 'c' # try .pyc file if .py does nto exists
                foo = imp.load_compiled('__init__', path)
            #foo = imp.load_source(md5.new(path).hexdigest() + '__init__', path)
            for file in foo.modules:
                # Load each profile class individually
                fooModule = ClassManager.load_module(file)
                for cls in dir(fooModule):          #<-- Loop over all objects in the module's namespace
                  cls = getattr(fooModule, cls)
                  if (inspect.isclass(cls)                # Make sure it is a class
                      and inspect.getmodule(cls) == fooModule ):  # Make sure it was defined in module, not just imported
                        yield cls
        except ImportError:
            print "Unable to import modules at: %s" % (path,)
            raise
        except Exception:
            print "Path error for: " + path
            #time.sleep(20)
            traceback.print_exc()
            raise

    @staticmethod
    def getClassListFromPath(path, class_type):
        list = []

        # Import profile modules and classes
        classes = ClassManager.getClasses(os.path.realpath(path))
        for cls in classes:
            if issubclass(cls, class_type):  # Make sure it is a Calculator class
                # Add everything to list
                list.append(cls())

        return list

    @staticmethod
    def mergeClassListsFromPaths(common_path, rev_path, class_type):
        try:
            list = []

            # Find all .py files for this family in common
            path = common_path
            common_list = ClassManager.getClassListFromPath(path, class_type)

            # Find all .py files for this family and revision in part revision
            path = rev_path
            rev_list = ClassManager.getClassListFromPath(rev_path, class_type)

            # Loop through common phys and remove and parent classes from part rev specific instance
            list = ClassManager.merge_lists_classes(common_list, rev_list)

            return list
        except ImportError:
            print "Unable to import modules at: %s" % (path,)
        except Exception:
            traceback.print_exc()

    @staticmethod
    def merge_lists_classes(common_classes, part_specific_classes):
        # Loop through common calculators and remove and parent classes from part rev specific instance
        for common_class in common_classes[:]:
            for part_specific_class in part_specific_classes:
                parent_classes = part_specific_class.__class__.__bases__
                for parent_class in parent_classes:
                    parent_class_name = str(parent_class.__name__)
                    common_calculator_name = str(common_class.__class__.__name__)
                    if (parent_class_name in common_calculator_name):
                        common_classes.remove(common_class)
                        break
        list = []
        list.extend(part_specific_classes)
        list.extend(common_classes)
        return list
