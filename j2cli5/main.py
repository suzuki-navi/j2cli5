import sys
import yaml
import jinja2

def main():
    templateFile, configFiles = parse_args()
    with open(templateFile, "r") as fh:
        templateStr = fh.read()
    template = jinja2.Template(templateStr)
    configData = build_config(configFiles)
    sys.stdout.write(template.render(configData))

def parse_args():
    template = None
    configs = []
    argCount = len(sys.argv)
    i = 1
    while i < argCount:
        a = sys.argv[i]
        if a == "-":
            a = "/dev/stdin"
        if a.startswith("-"):
            raise Exception(f"Unknown option: {a}")
        elif template == None:
            template = a
        else:
            configs.append(a)
        i += 1
    return [template, configs]

def build_config(config_files):
    result = {}
    for f in config_files:
        with open(f, "r") as fh:
            config = yaml.safe_load(fh.read())
        for key, value in config.items():
            result[key] = value
    return result

