import subprocess
import time

iterations = 1000  # Change this to the number of times you want to run the command
delay = 1  # Delay in seconds

for _ in range(iterations):
    subprocess.run(["python3", "run.py"])
    time.sleep(delay)
a