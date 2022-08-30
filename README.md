# Generate Fast API

Generate FastApi based CRUD operations with simple model.

This project currently works with json file and create fastapi code with MongoDB support.

<br/>

# Give A Shot ?

## Vscode Launch

- First generate your model.json file based on example.model.json in core folder.

- Open Core file in vsCode you will see launch option.

## Manual

```
cd core
```

```
Generate your model.json file.
```

```
python api_generator.py
```

This file will generate dist file you can open that file and run your fastapi app.

- You can use vscode task and launch part. 

```
click ctrl + shift + b for create virtualenv with requirements.
```

```
Click vscode Launch section to run app.
```


Don't you know how to run FastAPI app. Visit this page [FastApi](https://fastapi.tiangolo.com/tutorial/)


## TO DO
 - TAG Support.
 - Model Seperation for update.
 - ~~Add Delete Support~~
 - Add Soft Delete Support
 - UI Support.
 - Add More Option.
