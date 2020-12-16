import os


def get_environment_variable(varname):
    try:
        env_var_str = os.environ[varname]
        print(f"{varname} found:\n{env_var_str}")
        return env_var_str
    except KeyError:
        print(f"{varname} not set in environment!\n\
        To set environment variable {varname}\n\n\
            If you haven't already, create file '.env' in repository root ({os.getcwd()})\n\
                $ touch .env\n\n\
            Enter the following in .env:\n\
                {varname}=<your_connection_string>\n\n\
        After the environment variable is created, the virtual env or shell (e.g. pipenv) needs to be closed and reloaded \
        to take the environment variable into account.")