#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

if __name__ == '__main__':
    argv = sys.argv
    project_name = ""
    if len(argv) > 1:
        project_name = argv[1]
    else:
        while len(project_name) == 0:
            print "Input project name"
            project_name = raw_input("--> ")

    if os.path.exists(project_name):
        sys.stderr.write("File exsists\n")
        sys.exit(-1)

    os.mkdir(project_name)
    os.chdir(project_name)
    os.makedirs("src/main/java")
    os.makedirs("src/main/scala")
    os.makedirs("src/test/java")
    os.makedirs("src/test/scala")
    os.makedirs("project")

    build_sbt = open("build.sbt", 'w')
    build_sbt.write('name := "' + project_name + '"\n')
    build_sbt.write("\n")
    build_sbt.write('version := "0.1"\n')
    build_sbt.write("\n")
    build_sbt.write('scalaVersion := "2.11.0"\n')
    build_sbt.write("\n")

    plugin_sbt = open("project/plugins.sbt", 'w')
    plugin_sbt.close()

    gitignore = open(".gitignore", 'w')
    gitignore.write("*.class\n")
    gitignore.write("*.log\n")
    gitignore.write("\n")
    gitignore.write(".cache/\n")
    gitignore.write(".history/\n")
    gitignore.write(".lib/\n")
    gitignore.write("dist/*\n")
    gitignore.write("target/\n")
    gitignore.write("project/boot/\n")
    gitignore.write("project/plugins/project/\n")
    gitignore.close()

