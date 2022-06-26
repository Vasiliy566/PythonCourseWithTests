import os
import subprocess

if not os.path.isfile("1/"):
  raise Exception("Create forlder 1/ for firts task")

output = subprocess.check_output("python3 1/example.py", shell=True)
assert output == "Hello world", "Your program should return 'Hello World'"
