import inspect
from IPython.display import display, Markdown

def display_signature(obj):
    s = inspect.signature(obj)
    name = getattr(obj, '__name__', str(obj))
    _str = f"### {name}\n\n"
    for param_name, param in s.parameters.items():
        default = f" = {param.default}" if param.default != inspect.Parameter.empty else " *"
        annotation = f": {param.annotation}" if param.annotation != inspect.Parameter.empty else ""
        _str += f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**{param_name}**{annotation}{default}\n\n"

    display(Markdown(_str))