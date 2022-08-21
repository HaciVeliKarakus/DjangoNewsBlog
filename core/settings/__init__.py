from split_settings.tools import include

base_setttings = [
    "dev/common.py",  # standart django settings
    "dev/database.py"
]
include(*base_setttings)
