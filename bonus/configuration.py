from ultra_config import GlobalConfig

from bonus import default_settings

# Loads all default settings, then overrides with
# env variables that begin with MY_APP and configuration
# from a json file
GlobalConfig.load(default_settings=default_settings,
                  env_var_prefix='MY_APP',
                  json_file='/opt/my_app/config.json')


@GlobalConfig.inject(some_value='OTHER_VAR')
def some_func(arg1, some_value=None):
    print(arg1, some_value)


if __name__ == '__main__':
    # prints: '1, some_val' Using the configuration for
    some_func(1)

    # prints: '2, manual intervention' ignoring the configuration.  Very useful for testing
    some_func(2, 'manual intervention')
