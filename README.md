# NEA--Topology-Blueprinter

##Overiew
This project is a network topology designer that allows users to create a blueprint of their network without any of the physical equipment.This was developed for my A-level computer science coursework and was created over the course of about 6 months.

##Project Status
Currently finished ,however definitely will return to this idea to develop further

##Features
-Storage of Topologies(in text files)
-Loading of Topologies from storage
-Graphical Viewing of topologies
-editing of devices(adding/removing connections)
-Custom device creations(picking own device specifications)
-GUI used for user interactions

##Tech Stack
-only Python was used for this project

-library called DearPyGUI was used for the creation of the GUI
- OS library was used for file storage (creating file paths etc)
-any other libraries are those included with the installation of python

-Topologies created from the project is stored in a folder where each file is a .txt
-inside the .txts the topologies are stored as adjacency lists

-Git was used for version control and VS Code was used as my editor
-Github has been used for distribution and access to the project over different machines

##Layout
+---------------------+
|   User Interface    |
|      (DearPyGUI)    |
+---------------------+
            |
            v
+---------------------+
|  Application Logic  |
| (Validation, Tasks) |
+---------------------+
            |
            v
+---------------------+
|    Data Storage     |
|     (txt File)      |
+---------------------+


##Installation Instructions
Must have python installed
https://www.python.org/downloads/

Must have DearPyGui installed
https://pypi.org/project/dearpygui/

then clone the repo using the terminal
then to use the program 
run in terminal:

python Main.py

from the NEA directory

##Troubleshooting
To run/load the program may take some time from running it so you must be patient or close and re run if a popup does not appear
