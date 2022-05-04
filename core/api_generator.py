import os
from create_folders import main as create_folder
from json_operations import main as json_operations
from create_models import main as create_models
from create_views import main as create_views
from folders import models_folder, views_folder, dist_folder
from create_main import main as create_main


def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')


def main():
    create_folder()
    data = json_operations()
    models_file_data = create_models(data)
    with open(os.path.join(models_folder, "models.py"), "w") as file:
        file.write(models_file_data.__str__())

    view_files = []
    for model in data:
        model_name = model.get("model_name").strip()
        view_file_name = camel_to_snake(model_name).lower()
        view_files.append(view_file_name)
        url = model.get("url")
        collection = model.get("collection")
        view_code = create_views(model_name, url, collection)
        with open(os.path.join(views_folder, f"{view_file_name}.py"), "w") as file:
            file.write(view_code.__str__())

    main_file_data = create_main(view_files)

    with open(os.path.join(dist_folder, "main.py"), "w") as file:
        file.write(main_file_data.__str__())


if __name__ == "__main__":
    main()
