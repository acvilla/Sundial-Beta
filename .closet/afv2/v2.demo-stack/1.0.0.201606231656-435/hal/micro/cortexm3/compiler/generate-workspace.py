#!/usr/bin/python

###############
# generate-workspace.py
#
# This script will create project files to build an application given a Jam
# output directory. This is an unfinished port of the old perl version that's
# supposed to be more generic. It's basically here because I didn't want to
# heavily modify the Perl code to work with GCC Makefiles, but I never took the
# time to make this work for both IAR and GCC so that I could eliminate the Perl
# version (bryan - 2015_07_07).
# 
###############

import os
import sys
import re
import argparse

fixZnetZip = None

def fixSubmodulesDirectory(text):
  text = text.replace("submodules/base", "")
  return text

def headerDefFixer(m):
  pathModifier = "$$--rootPath--$$/"
  return '-D%s_%s=\\"%s%s\\"' % (m.group(1), m.group(2), pathModifier, m.group(3))

def fixDirectories(text, outDir, replacePaths=None):
  # Fix the PLATFORM_HEADER and BOARD_HEADER becuase they want to be difficult
  # NOTE: Do this first so that rootPath fixes things below
  regex = re.compile("-D(\w+)_(HEADER|LIST|CONFIG)=\"([^\s]+)\"")
  text = regex.sub(headerDefFixer, text)

  # Change all $$--rootPath--$$ specifiers to make things relative to where we
  # put the makefile
  text = text.replace("$$--rootPath--$$", outDir)

  # Allow fixing of paths like submodules/base/* to what they are in the release
  if replacePaths is not None:
    for (old, new) in replacePaths:
      text = text.replace(old, new)

  return text

def iarHandler(name, text, outDir):
  return text

def makeHandler(name, text, outDir):
  if fixZnetZip:
    replacePaths = [("submodules/base", "")]
  else:
    replacePaths = None

  # Fix all the root path specifiers
  text = fixDirectories(text, outDir, replacePaths)

  # Make requires multi-line variables to have proper '\' continuations
  lines = text.splitlines()
  text = " \\\n".join(lines)

  return text

def fillTemplate(file, directory, outDir='.', handler=None):
  replaceRegex = re.compile("\$\$--(.*)--\$\$")
  outputText = ""

  # Read in the template file
  with open(file, 'r') as f:
    # Read in the whole template file
    outputText = f.read()

  # Find all of the replacement blocks in the template file
  matches = replaceRegex.findall(outputText)
  matches = list(set(matches))

  for match in matches:
    replaceText = ""
    replaceFile = os.path.join(directory, match + ".build")

    # Attempt to find this build output file
    if os.path.isfile(replaceFile):
      with open(replaceFile, 'r') as f:
        replaceText = f.read()

    # Allow a special handler function to be called to modify the replacement
    # text before inserting it in the file. This allows for different compilers
    # and other modifications we need to make while creating the project file
    if handler is not None:
      replaceText = handler(match, replaceText, outDir)

    # Replace this text in the template file
    outputText = outputText.replace("$$--%s--$$" % match, replaceText)

  return outputText

def main(argv):
  # Configure the argument parser
  parser = argparse.ArgumentParser(description="Script to create build project files from a Jam output folder.")
  parser.add_argument('directory', type=str, help="The Jam output directory to create a workspace for.")
  parser.add_argument('--type', type=str, default=None, choices=["iar", "make"], help="The type of output file to generate (only make supported right now)")
  parser.add_argument('--template', type=str, action='append', help="A template file to include in the output. This is mainly for debugging.")
  parser.add_argument('--output', type=str, default=None, help="The output file name for the project file.")  
  parser.add_argument('--fixZnetZip', action='store_true', help="Fix the output paths for Znet and Zip to not have submodules/base in them.")
  a = parser.parse_args(argv)

  # Make sure the directory exists
  if not os.path.isdir(a.directory):
    print "Error: Invalid jam output directory '%s' specified" % (a.directory)
    return 1

  # Get a list of all the template files to fill in
  templates = a.template

  # Store this in a global variable for use later
  global fixZnetZip
  fixZnetZip = a.fixZnetZip

  # @TODO: Maybe add automatic templates based on the type they selected
  
  # Find files named *.build
  for file in templates:
    # Construct the argument list to pass to the template engine
    kwargs = {"file":file, "directory":a.directory}
    kwargs["handler"] = makeHandler
    if a.output is not None:
      kwargs["outDir"] = os.path.relpath(".", os.path.dirname(a.output))

    fileText = fillTemplate(**kwargs)

    # Save the new output file text to a project with the name of the target
    if a.output is not None:
      (root, ext) = os.path.splitext(file)
      if a.output.endswith("Makefile") and ext == ".make":
        name = a.output
      else:
        name = a.output + ext
      with open(name, 'w') as f:
        f.write(fileText)
    else:
      print fileText  

  return 0

# Call main if necessary
if __name__ == '__main__':
  main(sys.argv[1:])
