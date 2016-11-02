import yaml

with open('config_vars.yaml', 'r') as stream:
    try:
        print yaml.load(stream)['Ovs']
    except yaml.YAMLError as exc:
        print exc
