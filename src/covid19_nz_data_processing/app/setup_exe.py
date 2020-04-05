import sys
from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files': [
            (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
            (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))
         ],
        'packages': ["pandas", "numpy", "scipy", "matplotlib", "requests", "xlrd", "bs4"],
        'includes': 'atexit',
    },
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('app.py', base=base)
]

setup(name='matplotlib_embedding_in_Tkinter',
      version='0.1',
      description='Sample cx_Freeze matplotlib embedding in Tkinter script',
      options=options,
      executables=executables
      )