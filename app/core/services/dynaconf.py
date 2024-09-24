# config.py
from dynaconf import Dynaconf

settings = Dynaconf(
    load_dotenv=True,
    lowercase_read=True,
    environments=True,
    default_settings_paths="settings.toml",
)
