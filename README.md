# Mock CoreData Preview Server
Mock preview server for development. It will always serve the same image for every page requested.

### Installing
Create a virtualenv with python 2 or 3 and install requirements into that.
```
pip install -r requirements.txt
```

### Running
Stop local previewserver (if running) and run the mock one.
```
python prev.py
```

## Docker
``
docker run -e PORT=8000 --detach --publish 1337:8000 mock-preview
```
