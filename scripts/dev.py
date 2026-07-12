import subprocess
import sys

tailwind = subprocess.Popen(["npm.cmd", "run", "dev"])

try:
    subprocess.run([sys.executable, "main.py"])
except KeyboardInterrupt:
    pass
finally:
    tailwind.terminate()
    tailwind.wait()
