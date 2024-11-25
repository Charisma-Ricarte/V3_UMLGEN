import ast

def parse_class_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML class diagram.
    """
    tree = ast.parse(source_code)
    uml_code = "@startuml\n"
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            uml_code += f"class {class_name} {{\n"
            
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    uml_code += f"  + {method_name}()\n"
            uml_code += "}\n"
            
            for base in node.bases:
                if isinstance(base, ast.Name):
                    parent_class = base.id
                    uml_code += f"{class_name} -|> {parent_class}\n"
    
    uml_code += "@enduml"
    return uml_code

def parse_sequence_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML sequence diagram.
    """
    tree = ast.parse(source_code)
    uml_code = "@startuml\n"
    participants = set()
    calls = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            caller = "User"
            callee = node.name
            participants.add(caller)
            participants.add(callee)
            calls.append(f"{caller} -> {callee} : call {callee}()\n")
    
    for participant in participants:
        uml_code += f"participant {participant}\n"
    uml_code += "".join(calls)
    uml_code += "@enduml"
    return uml_code

def parse_usecase_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML use case diagram.
    """
    tree = ast.parse(source_code)
    uml_code = "@startuml\n"
    uml_code += "actor User\n"
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            use_case = node.name
            uml_code += f"User -> ({use_case})\n"
    
    uml_code += "@enduml"
    return uml_code

def parse_activity_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML activity diagram.
    """
    tree = ast.parse(source_code)
    uml_code = "@startuml\nstart\n"
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            activity = node.name
            uml_code += f":{activity};\n"
    
    uml_code += "stop\n@enduml"
    return uml_code

def parse_component_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML component diagram.
    """
    tree = ast.parse(source_code)
    uml_code = "@startuml\n"
    
    components = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            components.append(node.name)
    
    for component in components:
        uml_code += f"component {component}\n"
    
    if len(components) > 1:
        for i in range(len(components) - 1):
            uml_code += f"{components[i]} --> {components[i+1]}\n"
    
    uml_code += "@enduml"
    return uml_code

def parse_deployment_diagram(source_code):
    """
    Generates a PlantUML deployment diagram.
    """
    return "@startuml\nnode Server\nnode Client\nClient --> Server : Communication\n@enduml"

def parse_state_diagram(source_code):
    """
    Parses Python source code and generates a PlantUML state diagram.
    """
    uml_code = "@startuml\n[*] --> State1\n"
    
    for node in ast.walk(ast.parse(source_code)):
        if isinstance(node, ast.FunctionDef):
            uml_code += f"State1 --> {node.name}\n"
    
    uml_code += "@enduml"
    return uml_code

def parse_timing_diagram(source_code):
    """
    Generates a PlantUML timing diagram.
    """
    return "@startuml\ntitle Timing Diagram\n@0\nobject A\nobject B\nA is Active @1\nB is Inactive @2\n@enduml"

def generate_uml_plantuml(python_code, diagram_type):
    """
    Generates UML code based on the selected diagram type.
    """
    if diagram_type == "Class Diagram":
        return parse_class_diagram(python_code)
    elif diagram_type == "Sequence Diagram":
        return parse_sequence_diagram(python_code)
    elif diagram_type == "Use Case Diagram":
        return parse_usecase_diagram(python_code)
    elif diagram_type == "Activity Diagram":
        return parse_activity_diagram(python_code)
    elif diagram_type == "Component Diagram":
        return parse_component_diagram(python_code)
    elif diagram_type == "Deployment Diagram":
        return parse_deployment_diagram(python_code)
    elif diagram_type == "State Diagram":
        return parse_state_diagram(python_code)
    elif diagram_type == "Timing Diagram":
        return parse_timing_diagram(python_code)
    else:
        raise ValueError(f"Unsupported diagram type: {diagram_type}")
