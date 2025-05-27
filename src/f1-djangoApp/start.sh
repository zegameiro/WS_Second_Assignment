#!/bin/bash

# Start Tailwind and get its PID
python manage.py tailwind start &
TAILWIND_PID=$!

# Start Django runserver
python manage.py runserver &
RUNSERVER_PID=$!

# Handle script exit to kill both processes
trap "kill $TAILWIND_PID $RUNSERVER_PID" EXIT

# Wait for both to finish (or one to exit)
wait
