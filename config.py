#####################################################
#           Imports                                 #
#####################################################

# Libraries
import os
import logging

# Module import of env.py for LocalConfig class
import env

#####################################################
#           Functions                               #
#####################################################


def if_in_environ(key):
    res = os.environ[key] if key in os.environ else ""
    return res

#####################################################
#           Config classes                          #
#####################################################


class LocalConfig(object):
    config_variables = [x for x in env.__dict__.keys() if not x.startswith("__")]
    for variable in config_variables:
        globals()[variable] = env.__dict__[variable]


class ProdConfig(object):
    config_variables = [x for x in env.__dict__.keys() if not x.startswith("__")]
    for variable in config_variables:
        globals()[variable] = if_in_environ(variable)


config = {
    "local": "config.LocalConfig",
    "prod": "config.ProdConfig"
}


def configure_app(app, run_mode):
    config_name = os.getenv("FLASK_CONFIGURATION", run_mode)
    app.config.from_object(config[config_name])
