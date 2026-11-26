import ast

def get_function_details(code):
    tree = ast.parse(code)

    function_details = {}
    lines=code.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            arguments = []
            details={}
            for arg in node.args.args:
                arguments.append(arg.arg)
            details['arguments'] = arguments
            details['lineno'] = node.lineno
            source_lines=lines[node.lineno-1:node.end_lineno]
            source="\n".join(source_lines)
            details['source'] = source
            function_details[node.name]=details


    return function_details


if __name__ == "__main__":
    code = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

    result = get_function_details(code)
    print(result)