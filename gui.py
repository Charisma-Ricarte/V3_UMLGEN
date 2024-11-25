import tkinter as tk
from tkinter import filedialog
from uml_generator import generate_uml_plantuml

def upload_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        with open(filepath, "r") as file:
            python_code.set(file.read())

def generate_diagram():
    try:
        diagram_type = diagram_type_var.get()
        python_code_text = python_code.get()
        uml_code = generate_uml_plantuml(python_code_text, diagram_type)
        uml_code_display.config(state=tk.NORMAL)
        uml_code_display.delete(1.0, tk.END)
        uml_code_display.insert(tk.END, uml_code)
        uml_code_display.config(state=tk.DISABLED)
    except Exception as e:
        uml_code_display.config(state=tk.NORMAL)
        uml_code_display.delete(1.0, tk.END)
        uml_code_display.insert(tk.END, f"An error occurred: {e}")
        uml_code_display.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("UML Generator")

# Python Code
python_code = tk.StringVar()

tk.Button(root, text="Upload Python File", command=upload_file).pack()

tk.Label(root, text="Select Diagram Type:").pack()
diagram_type_var = tk.StringVar(value="Class Diagram")
diagram_types = [
    "Class Diagram", "Sequence Diagram", "Use Case Diagram",
    "Activity Diagram", "Component Diagram", "Deployment Diagram",
    "State Diagram", "Timing Diagram"
]
tk.OptionMenu(root, diagram_type_var, *diagram_types).pack()

tk.Button(root, text="Generate Diagram", command=generate_diagram).pack()

tk.Label(root, text="Generated PlantUML Code:").pack()
uml_code_display = tk.Text(root, height=20, width=80, state=tk.DISABLED)
uml_code_display.pack()

tk.Label(
    root, text="Copy the code above and visit https://www.plantuml.com/plantuml to render your UML diagram."
).pack()

root.mainloop()
