
import logging

from code_block import CodeBlock, CodeBreak
from code_block import Code


logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(process)d | %(message)s',)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def main(models, port=8000):
    logger.info("Started to Create Main File")
    logger.info("Generating imports for Main File")
    import_list = [
        "import uvicorn",
        "from fastapi import FastAPI",
        "from fastapi.responses import JSONResponse",
        "from fastapi.middleware.cors import CORSMiddleware",
        "from fastapi.exceptions import RequestValidationError",
        "from fastapi.encoders import jsonable_encoder",
        "from configs.config import prefix",
    ]
    imports = Code("", import_list)
    logger.info("Generating Codes for Main File")

    code = Code('''app=FastAPI(
            title="Develop FastApi CRUD functions with model",
            description="""Generate Fast API \n\n furkanozkaya.com \n\n github.com/furkanozkaya""",
            version="0.0.1"
        )''')
    code += Code('# Changing 422 Unprocessable Entity to  to 400 Bad Request')
    code += Code('''origins = ["*"]''')

    code += Code('''app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )''')
    code += Code('@app.exception_handler(RequestValidationError)')
    code += CodeBlock('async def validation_exception_handler(request, exc)',
                      ['content = jsonable_encoder({"detail": exc.errors()})',
                       'return JSONResponse(content=content, status_code=400)'])

    for model in models:
        imports += Code(f'from views.{model} import router as {model}')
        code += Code(f'app.include_router({model}, prefix=prefix)')
    imports += CodeBreak()
    code += CodeBreak()
    code += CodeBlock('if __name__ == "__main__"', [f'uvicorn.run(app, host="0.0.0.0", port={port})'])

    return imports + code
