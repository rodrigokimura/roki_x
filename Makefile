DEVICE_PATH := /run/media/$(USER)/CIRCUITPY

install:
	@circup install -a

update:
	@circup update

ls:
	ls $(DEVICE_PATH)

put:
	@rm $(DEVICE_PATH)/*.py -vf
	@rm $(DEVICE_PATH)/*.json -vf
	@rm $(DEVICE_PATH)/*.toml -vf
	@cp src/* $(DEVICE_PATH)/ -rv

check:
	@rshell -l

run:
	@ampy -p /dev/ttyACM1 run src/code.py

test:
	@pipenv run pytest --cov src/ --cov-report html --cov-report term

reset:
	@ampy -p /dev/ttyACM1 reset

lint:
	@pipenv run black .
	@pipenv run isort .

keys:
	@KEYS=$$(ampy -p /dev/ttyACM1 run src/all_keys.py); echo "const KEYS = $$KEYS;" > config/keys.js
	@echo "Keys saved!"
	@echo "Restarting keyboard runtime..."
	@ampy -p /dev/ttyACM1 run src/code.py
