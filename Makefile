.PHONY: start

install:
	pip install -r requirements.txt

start:
	python3 ccws/app.py
