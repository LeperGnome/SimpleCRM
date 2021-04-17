import os


def get_settings_module() -> str:
    cur_file_dir = os.path.dirname(os.path.abspath(__file__))

    if os.path.isfile(os.path.join(cur_file_dir, 'local.py')):
        settings_type = 'local'
    elif os.path.isfile(os.path.join(cur_file_dir, 'production.py')):
        settings_type = 'production'
    else:
        raise Exception('no settings file found')

    return f'SimpleCRM.settings.{settings_type}'
