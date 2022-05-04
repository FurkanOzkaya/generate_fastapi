import logging

from code_block import CodeBlock, CodeBreak
from code_block import Code

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(process)d | %(message)s',)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def main(data):
    logger.info("Started to Create Models")
    logger.info("Adding imports")
    imports = Code("from pydantic import BaseModel")
    imports += Code("from typing import Optional")
    imports += Code("from pydantic import *")
    imports += Code("from datetime import datetime", [CodeBreak()])

    model_list = []
    for model in data:
        model_name = model.get("model_name")
        args = model.get("args")
        argument_list = []
        for arg in args:
            name = arg.get("name")
            required = arg.get("required")
            arg_type = arg.get("type")
            if not required:
                argument = Code(f"{name}: Optional[{arg_type}]")
            else:
                argument = Code(f"{name}: {arg_type}")
            argument_list.append(argument)
        model = CodeBlock(f"class {model_name}(BaseModel)", argument_list)
        model_list.append(model)

    page = Code(imports.__str__(), model_list)
    return page
