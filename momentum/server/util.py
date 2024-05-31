# util.py
import os
import yaml
def get_config(env, config_resource):
    # Load config options for the given environment
    config_dict = yaml.load(config_resource, Loader=yaml.Loader)
    try:
        config_dict = config_dict[env]
    except KeyError:
        raise KeyError("Invalid ENV value '{}' should be in {}, set using FLASK_ENV=value".format(
                    env, list(config_dict.keys())) )
    # Load any FLASK_ environment variables
    for key, value in os.environ.items():
        if key.startswith('FLASK_'):
            config_dict[key[6:]] = value
    # Load any env: values from the environment
    for key, value in config_dict.items():
        if isinstance(value, str) and value.startswith('env:'):
            config_dict[key] = os.environ[value[4:]]
    # Put the values into the application config
    print(config_dict)
    return config_dict
