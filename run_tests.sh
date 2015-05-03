#!/bin/bash
python sklDj/manage.py runserver &
python -m unittest discover sklDj/tests/
