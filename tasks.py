from invoke.context import Context
from invoke.tasks import task


def get_device_path(c: Context):
    name = "ROKI_X"
    for cmd in ["mount", "/sbin/mount"]:
        try:
            if r := c.run(cmd, hide=True):
                volumes = (v.split()[2] for v in r.stdout.splitlines())
                return next(v for v in volumes if v.endswith(name))
        except (FileNotFoundError, StopIteration):
            continue
    print("No device found.")


def get_serial_device(c: Context):
    vendor = "RokiX"
    intf = "CircuitPython CDC control"

    if r := c.run("rshell -l", hide=True):
        try:
            return next(
                d.split("@")[-1]
                for d in r.stdout.splitlines()
                if vendor in d and intf in d
            )
        except StopIteration:
            ...


def clean(c: Context):
    c.run(r"find ./ -name '*.pyc' -exec rm -f {} \;")
    c.run(r"find ./ -name '__pycache__' -exec rm -rf {} \;")


@task
def install(c: Context):
    """Install CircuitPython modules"""
    if DEVICE_PATH := get_device_path(c):
        commands = [
            f"circup --path {DEVICE_PATH} install --auto --auto-file code.py",
            f"circup --path {DEVICE_PATH} install --auto --auto-file firmware/kb.py",
            f"circup --path {DEVICE_PATH} install --auto --auto-file firmware/keys.py",
        ]
        for command in commands:
            c.run(command)


@task
def update(c: Context):
    """Update CircuitPython modules"""
    if DEVICE_PATH := get_device_path(c):
        c.run(f"circup --path {DEVICE_PATH} update")


@task
def put(c: Context, left=False, right=False):
    """Upload CircuitPython code to microcontroller"""
    if left + right != 1:
        print("Pass --left/-l or --right/-r flag")
        exit(1)

    side = "rl"[left]
    clean(c)
    if DEVICE_PATH := get_device_path(c):
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
        c.run(f"cp src/{side}_settings.toml {DEVICE_PATH}/settings.toml -v")


@task
def check(c: Context):
    """Check serial devices"""
    c.run("rshell -l")


@task
def run(c: Context):
    """Run code.py"""
    if SERIAL_DEVICE := get_serial_device(c):
        c.run(f"ampy -p {SERIAL_DEVICE} run src/code.py")


@task
def test(c: Context):
    """Run tests"""
    c.run("pytest --cov src/ --cov-report html --cov-report term", pty=True)


@task
def lint(c: Context):
    """Lint code"""
    c.run("pipenv run black .")
    c.run("pipenv run isort .")


@task
def config(c: Context, port=12_000):
    """Start configuration server"""
    c.run(f"pipenv run uvicorn src.config.main:app --port {port} --reload")
