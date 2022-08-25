import os
import json


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def main():
    file = os.path.join(CURRENT_PATH, "model.json")
    try:
        with open(file, "r") as file:
            data = file.read()
    except FileNotFoundError:
        logger.error("Please write your model.json file according to example.model.json")
    return json.loads(data)


if __name__ == "__main__":
    main()
