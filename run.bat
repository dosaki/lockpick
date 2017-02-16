@echo OFF

set FLASK_APP=index.py
IF "%1" == "debug" (
  set FLASK_DEBUG=1
) ELSE (
  set FLASK_DEBUG=0
)

flask run --host=0.0.0.0
