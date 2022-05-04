import os
from datetime import datetime
from uuid import uuid4


def date_to_iso_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
    except:
        date = datetime.strptime(
            f"{date}T12:00:30.575+00:00", '%Y-%m-%dT%H:%M:%S.%f%z')
    return date


def handle_id_for_model(data):
    if data:
        id = data.get("_id", None)
        if id:
            data["_id"] = str(data["_id"])
        return data


def handle_object_ids(datas):
    for data in datas:
        data = handle_id_for_model(data)
    return datas


def create_dir(dir):
    try:
        if not os.path.isdir(dir):
            os.makedirs(dir)
        return True
    except Exception as err:
        return False


def delete_file(file):
    try:
        if os.path.isfile(file):
            os.remove(file)
            return True
        else:
            return False
    except Exception as err:
        return False


def generate_unique_id():
    unique_id = uuid4()
    return str(unique_id)
