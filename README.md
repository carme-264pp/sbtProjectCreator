# SbtProjectCreator
---
This program is generated the directories and files needed for the sbt project.

## How to use
```
 $ sbt-create [project name]
```
 or
```
 $ sbt-create
  Input project name
  -> [project name]
```

## Directories and files
```
 [project name]/
  |-- build.sbt
  |-- project/
  |  `-- plugins.sbt
  `-- src/
     |-- main/
     |  |-- java/
     |  `-- scala/
     `-- test/
        |-- java/
        `-- scala/
```
