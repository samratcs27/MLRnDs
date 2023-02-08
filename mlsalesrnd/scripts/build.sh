#!/bin/bash

handle_error_if_any()
{
if [ $1 -eq 0 ]
then
  echo "Successfully executed step"
else
  # Redirect stdout from echo command to stderr.
  echo "Script exited with error."
  exit 1
fi
}

python setup.py install --force
