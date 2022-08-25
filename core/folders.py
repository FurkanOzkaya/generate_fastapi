import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


dist_folder = os.path.join(CURRENT_PATH, "dist")
vscode_folder = os.path.join(dist_folder, ".vscode")
database_folder = os.path.join(dist_folder, "database")
models_folder = os.path.join(dist_folder, "models")
configs_folder = os.path.join(dist_folder, "configs")
views_folder = os.path.join(dist_folder, "views")
utils_folder = os.path.join(dist_folder, "utils")
