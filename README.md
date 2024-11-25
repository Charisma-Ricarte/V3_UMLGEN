# V3_UMLGEN #
This program allows you to generate uml diagrams from Python source code by transforming the code into the format that  PlantUML uses.
PlantUML, is an open-source tool for rendering UML diagrams from plain text descriptions.

## Setup ##
Please read the requirements.txt 
  If there are issues with these installs We recommend trying pip install tkinter uml_generator
Once the code is put into your environment, We recommend using VS Studio
Run uml_generator.py
Run gui.py
Feel free to upload your own source code or use one of the provided templates
The reformated code is displayed simply copy the code with copy paste keyboard shortcut
Then paste the code to https://www.plantuml.com/
Then refresh to see your diagram

## Templates ##
There is templates for each diagram type, you can edit , delete , or keep them as reference if you are unfamillar with UML diagrams.

## Troubleshooting ##
**"Failed to generate UML" error** -> This could happen if the .py file contains syntax errors or is not formatted correctly.
**UML code is empty** -> Please make sure that the selected diagram type matches the structre of the .py code. For example if you choose a Class Diagram, the .py code should contain classes.
