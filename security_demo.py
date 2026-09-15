import subprocess


def safe_command(command_args):
    return subprocess.run(command_args, check=False)
