.PHONY: config clean

# DEVICE_PATH := /run/media/$(USER)/CIRCUITPY
DEVICE_PATH := /run/media/$(USER)/ROKI_X

check:
	@rshell -l

run:
	@ampy -p /dev/ttyACM1 run src/code.py

test:
	@pipenv run pytest --cov src/ --cov-report html --cov-report term

lint:
	@pipenv run black .
	@pipenv run isort .

config:
	@uvicorn src.config.main:app --port 12000 --reload
