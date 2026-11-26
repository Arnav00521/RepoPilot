import ast

def get_function_names(code):
    tree = ast.parse(code)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return functions


if __name__ == "__main__":
    code = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

    result = get_function_names(code)
    print(result)