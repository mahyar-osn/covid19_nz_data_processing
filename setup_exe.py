import distutils
import sys
from cx_Freeze import setup, Executable
import os.path
import opcode
distutils_path = os.path.join(os.path.dirname(opcode.__file__), 'distutils')


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


options = {
    'build_exe': {
        'include_files': [(distutils_path, 'distutils'), 'tk86t.dll', 'tcl86t.dll'],
        'excludes': ['distutils'],
        'packages': ["pandas", "numpy", "scipy", "matplotlib", "requests", "xlrd", "bs4", 'pkg_resources._vendor'],
        'includes': ['atexit', 'matplotlib.backends.backend_tkagg'],
    },
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('src/covid19_nz_data_processing/app/app.py', base=base)
]


setup(
    name="covid19_nz_data_processing",
    version="0.0.1",
    description="Simple script to automatically fetch, process, and plot the NZ covid-19 cases data",
    options=options,
    executables=executables
)