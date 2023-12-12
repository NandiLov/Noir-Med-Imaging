"""
Activate virtual environment. This can be used by Python scripts to
activate the virtual environment without sourcing the activate script.
"""

import os

venv_path = '/home/noirmed/Noir-Med-Imaging/venv'
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')

# Load the activate_this script
exec(open(activate_this).read(), {'__file__': activate_this})
