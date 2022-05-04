import os
import logging
import shutil
import time
from folders import *

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(process)d | %(message)s',)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def create_folder_structure():

    logger.info("Cleaning workspace folder 'dist' Please check if you have this folder")
    time.sleep(5)
    shutil.rmtree(dist_folder)

    logger.info("Creating Folders")

    folders = [
        dist_folder,
        database_folder,
        models_folder,
        configs_folder,
        views_folder,
        utils_folder
    ]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder, 777)

    logger.info("Creating Init Files")
    init_file = "__init__.py"
    init_paths = [
        os.path.join(dist_folder, init_file),
        os.path.join(database_folder, init_file),
        os.path.join(models_folder, init_file),
        os.path.join(configs_folder, init_file),
        os.path.join(views_folder, init_file),
        os.path.join(utils_folder, init_file)
    ]
    for path in init_paths:
        with open(path, 'a'):
            pass

    logger.info("Copying Common files")
    common_files_path = os.path.join(CURRENT_PATH, "common_files")
    common_functions_file = os.path.join(common_files_path, "common_functions.py")
    config_file = os.path.join(common_files_path, "config.py")
    exceptions_file = os.path.join(common_files_path, "exceptions.py")
    mongodb_functions_file = os.path.join(common_files_path, "mongodb_functions.py")
    singleton_file = os.path.join(common_files_path, "singleton.py")

    shutil.copy(common_functions_file, utils_folder)
    shutil.copy(exceptions_file, utils_folder)
    shutil.copy(singleton_file, utils_folder)
    shutil.copy(config_file, configs_folder)
    shutil.copy(mongodb_functions_file, database_folder)

    logger.info("Creating Folder Structure is Finished")
    logger.info("="*10)


def main():
    create_folder_structure()


if __name__ == "__main__":
    main()
