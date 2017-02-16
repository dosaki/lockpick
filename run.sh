#!/bin/bash

export FLASK_APP=index.py
if [ "$1" == "debug" ]; then
  export FLASK_DEBUG=1
else
  export FLASK_DEBUG=0
fi
flask run --host=0.0.0.0
