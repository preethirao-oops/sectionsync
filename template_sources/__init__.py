"""Load Jinja templates stored as individual Python modules."""

import importlib
import pkgutil


def get_templates():
    templates = {}
    for item in pkgutil.walk_packages(__path__, __name__ + "."):
        if item.ispkg:
            continue
        module = importlib.import_module(item.name)
        template_name = item.name[len(__name__) + 1:].replace(".", "/") + ".html"
        templates[template_name] = module.TEMPLATE_SOURCE
    return templates
