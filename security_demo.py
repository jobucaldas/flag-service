import subprocess


def unsafe_command(command):
    return subprocess.run(command, shell=True, check=False)
