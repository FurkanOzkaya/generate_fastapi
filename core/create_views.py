
import logging

from code_block import CodeBlock, CodeBreak
from code_block import Code

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(process)d | %(message)s',)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def main(model_name, url, collection_name):
    logger.info("Started to Create Views")
    logger.info("Generating imports")
    import_list = [
        f"from models.models import {model_name}",
        "from database.mongodb_functions import MongoDB",
        "from fastapi import APIRouter, Response,  status",
        "from starlette.responses import JSONResponse",
        "from fastapi.encoders import jsonable_encoder",
        "from utils.common_functions import handle_id_for_model, handle_object_ids",
        CodeBreak()
    ]
    imports = Code("", import_list)

    logger.info("Generating Codes for View File")
    code = Code("router = APIRouter()", [CodeBreak()])

    # Get All
    code += Code(f"""@router.get("/{url}/",
                responses={{200: {{"model": {model_name} }},
                       204: {{"desciption": "No Data"}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(CodeBlock("try", ["res = client.get_all_documents()", "res = handle_object_ids(list(res))"]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(CodeBlock("if res", ["return JSONResponse(status_code=status.HTTP_200_OK, content=res)"]))
    inner_code.append(CodeBlock("else", ["return Response(status_code=status.HTTP_204_NO_CONTENT)"]))
    code += CodeBlock("def get_all(response: Response)", inner_code)
    code += CodeBreak()

    # Get
    code += Code(f"""@router.get("/{url}/{{id}}",
            responses={{200: {{"model": {model_name}}},
                       204: {{"desciption": "No Data"}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(CodeBlock("try", ["res = client.find_with_object_id(id)", "res = handle_id_for_model(res)"]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(CodeBlock("if res", ["return JSONResponse(status_code=status.HTTP_200_OK, content=res)"]))
    inner_code.append(CodeBlock("else", ["return Response(status_code=status.HTTP_204_NO_CONTENT)"]))
    code += CodeBlock("def get(response: Response, id: str)", inner_code)
    code += CodeBreak()

    # Post
    code += Code(f"""@router.post("/{url}/",
            responses={{201: {{"model": {model_name}}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(CodeBlock("try", ["content = jsonable_encoder(content)", "client.insert_one(content)"]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(Code('return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": "SUCCESS"})'))

    code += CodeBlock(f"def post(response: Response, content: {model_name})", inner_code)
    code += CodeBreak()

    # Patch
    code += Code(f"""@router.patch("/{url}/",
            responses={{200: {{"model": {model_name}}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(CodeBlock("try", ["content = jsonable_encoder(content)", "client.update_one(id, content)"]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(Code('return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "SUCCESS"})'))

    code += CodeBlock(f"def patch(response: Response, id: str, content: {model_name})", inner_code)
    code += CodeBreak()

    # Put
    code += Code(f"""@router.put("/{url}/",
            responses={{200: {{"model": {model_name}}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(CodeBlock("try", ["content = jsonable_encoder(content)", "client.update_one(id, content)"]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(Code('return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "SUCCESS"})'))

    code += CodeBlock(f"def put(response: Response, id: str, content: {model_name})", inner_code)
    code += CodeBreak()

    code += Code(f"""@router.delete("/{url}/",
            responses={{200: {{"description": "Deleted Successfully"}},
                       400: {{"description": "Bad Request Please check data."}},
                       422: {{"description": "RESPONSE NOT USED"}},
                       500: {{"description": "Internal Server Error"}}}})""")
    inner_code = []
    inner_code.append(Code("client = MongoDB()"))
    inner_code.append(Code(f'client.connect_collection("{collection_name}")'))
    inner_code.append(
        CodeBlock(
            "try",
            ["res = client.delete_one(id)",
             CodeBlock(
                 "if res", ['return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "SUCCESS"})']),
             CodeBlock(
                 "else",
                 ['return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={"status": "Doesn\'t Exist"})'])]))
    inner_code.append(
        CodeBlock(
            "except Exception as err",
            ['return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": f"{err}"})']))
    inner_code.append(Code('return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "SUCCESS"})'))

    code += CodeBlock(f"def delete(response: Response, id: str)", inner_code)
    code += CodeBreak()

    return imports + code
