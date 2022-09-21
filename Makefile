# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

pylint: venv
	./$(VENV)/bin/pylint --disable=C0303,R0903,R0915,C0103,E1101,E0102,R0913,W0123 simulation map population

tests: venv
	./$(VENV)/bin/python3 -m unittest

run: venv
	./$(VENV)/bin/python3 app.py

wsgi: venv
	./$(VENV)/bin/python3 -m flask --app web run

init-db: venv
	./$(VENV)/bin/python3 -m flask --app web init-db

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

# make sure that all targets are used/evaluated even if a file with same name exists
.PHONY: all venv run clean tests
