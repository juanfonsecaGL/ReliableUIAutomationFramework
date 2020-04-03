import os

def get_project_path():
    abs_filepath = os.path.abspath(__file__)
    file_dir = os.path.dirname(abs_filepath)
    parent_dir = os.path.dirname(file_dir)
    return parent_dir


def move_from_feaures_or_configs_dir_to(new_dir):
    os.chdir(get_project_path()+"/"+new_dir)


def move_from_output_dir_to_failed_scenarios_screenshots():
    if not os.path.exists("failed_scenarios_screenshots"):
        os.makedirs("failed_scenarios_screenshots")
    else:
        pass
    os.chdir("failed_scenarios_screenshots")


def move_from_failed_scenarios_screenshots_dir_to__output():
    os.chdir("..")


def create_dir_failed_scenarios():
    if not os.path.exists("failed_scenarios_zip_runs"):
        os.makedirs("failed_scenarios_zip_runs")
