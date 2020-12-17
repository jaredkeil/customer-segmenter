import os
from customerSeg.config import root

def get_env_var(varname):
    try:
        env_var_str = os.environ[varname]
        print(f"{varname} found:\n{env_var_str}")
        return env_var_str
    except KeyError:
        print(f"""
        {varname} not found in environment!
        To set environment variable {varname} :
            Ensure .env file exists in repository root ({root})
                $ touch .env
            Enter the value for varibale in .env:
                VARNAME=value
        After the environment variable is created, the virtual env or shell (e.g. pipenv)
        needs to be closed and reloaded to take the environment variable into account.""")