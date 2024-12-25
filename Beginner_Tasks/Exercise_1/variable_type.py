
from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str
x = input("Enter the variable: ")
print(x ,",datatype is",get_type(x))