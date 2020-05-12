activate_this_file = "/env/bin/activate_this.py"

execfile(activate_this_file, dict(__file__=activate_this_file))

import subprocess

python_bin = "/env/bin/python3"
script_file = ".git/hooks2.py"

subprocess.Popen([python_bin, script_file])
