import json
from utils.directory_handler import move_from_feaures_or_configs_dir_to


def loading_userdata_from_json(context):
    try:
        move_from_feaures_or_configs_dir_to("configs")
        userdata = context.config.userdata
        configfile = userdata.get("configfile", "userconfig.json")
        more_userdata = json.load(open(configfile))
        context.config.update_userdata(more_userdata)
        context.logger = None
        return context
    except Exception as e:
        print(str(e))
