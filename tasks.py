from invoke.context import Context
from invoke.tasks import task


def get_device_path(c: Context):
    name = "ROKI_X"
    for cmd in ["mount", "/sbin/mount"]:
        try:
            if r := c.run(cmd):
                volumes = (v.split()[2] for v in r.stdout.splitlines())
                return next(v for v in volumes if v.endswith(name))
        except (FileNotFoundError, StopIteration):
            continue


@task
def install(c: Context):
    DEVICE_PATH = get_device_path(c)
    commands = [
        f"circup --path {DEVICE_PATH} install --auto --auto-file code.py",
        f"circup --path {DEVICE_PATH} install --auto --auto-file firmware/kb.py",
        f"circup --path {DEVICE_PATH} install --auto --auto-file firmware/keys.py",
    ]
    for command in commands:
        c.run(command)


@task
def update(c: Context):
    DEVICE_PATH = get_device_path(c)
    c.run(f"circup --path {DEVICE_PATH} update")


@task
def clean(c: Context):
    c.run(r"find ./ -name '*.pyc' -exec rm -f {} \;")
    c.run(r"find ./ -name '__pycache__' -exec rm -rf {} \;")


@task
def put(c: Context, left=True):
    DEVICE_PATH = get_device_path(c)
    commands = [
        f"rm {DEVICE_PATH}/firmware/*.py -vf",
        f"rm {DEVICE_PATH}/*.py -vf",
        f"rm {DEVICE_PATH}/*.json -vf",
        f"mkdir -p {DEVICE_PATH}/firmware",
        f"cp src/firmware/* {DEVICE_PATH}/firmware/ -rv",
        f"cp src/code.py {DEVICE_PATH}/code.py -v",
        f"cp src/boot.py {DEVICE_PATH}/boot.py -v",
        f"cp config.json {DEVICE_PATH}/config.json -v",
    ]
    for command in commands:
        c.run(command)

    c.run(f"rm {DEVICE_PATH}/settings.toml -vf")
    c.run(f"cp src/{'rl'[left]}_settings.toml {DEVICE_PATH}/settings.toml -v")


@task
def check(c: Context):
    c.run("rshell -l")
