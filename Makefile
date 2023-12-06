.PHONY: config clean

DEVICE_PATH := /run/media/$(USER)/CIRCUITPY
# DEVICE_PATH := /run/media/$(USER)/ROKI_X

install:
	@circup install --auto --auto-file code.py
	@circup install --auto --auto-file firmware/kb.py
	@circup install --auto --auto-file firmware/keys.py

update:
	@circup update

ls:
	ls $(DEVICE_PATH)

put: clean
	@rm $(DEVICE_PATH)/firmware/*.py -vf
	@rm $(DEVICE_PATH)/*.py -vf
	@rm $(DEVICE_PATH)/*.json -vf
	@mkdir -p $(DEVICE_PATH)/firmware
	@cp src/firmware/* $(DEVICE_PATH)/firmware/ -rv
	@cp src/code.py $(DEVICE_PATH)/code.py -v
	@cp src/boot.py $(DEVICE_PATH)/boot.py -v
	@cp config.json $(DEVICE_PATH)/config.json -v

lput: put
	@rm $(DEVICE_PATH)/settings.toml -vf
	@cp src/l_settings.toml $(DEVICE_PATH)/settings.toml -v

rput: put
	@rm $(DEVICE_PATH)/settings.toml -vf
	@cp src/r_settings.toml $(DEVICE_PATH)/settings.toml -v

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

config:
	@uvicorn src.config.main:app --port 12000 --reload

clean:
	@echo "Removing cache files..."
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
