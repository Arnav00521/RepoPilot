import ast

def get_function_details(code):
    tree = ast.parse(code)

    function_details = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name) 
            arguments = []
            details={}
            for arg in node.args.args:
                arguments.append(arg.arg)
            details['arguments'] = arguments
            details['lineno'] = node.lineno
            function_details[node.name]=details


    return function_details


if __name__ == "__main__":
    code = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

    result = get_function_names(code)
    print(result)