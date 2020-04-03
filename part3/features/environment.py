import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import utils, userdata


def before_scenario(context, scenario):
    userdata.loading_userdata_from_json(context)
    utils.setup_browser(context)

def after_scenario(context, scenario):
    utils.clean_browser(context)   
