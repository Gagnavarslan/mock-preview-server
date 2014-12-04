# Mock Coredata Preview Server
Mock preview server for development. It will always server the same image for every page requested.

### Installing
```
virtualenv .
bin/pip install -r requirements.txt
```

### Running
Stop local previewserver if running then run the mock one
```
bin/python prev.py
```

It's best to run inside a screen/tmux session to be able to see the output but not have it take over the current session.  

Starting inside screen is simple

```
screen -d -m bin/python prev.py
```

And to attach screen again to stop the process/session it's simply

```
screen -r
```
