import sys
from cx_Freeze import setup, Executable

import os
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
#os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
#os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('clock.py', base=base,icon=r"C:\Users\Ashwani\Desktop\installer\Startup.ico",
                   shortcutName="MyClock",
                   shortcutDir="DesktopFolder")]

setup(name='Techsrijan Clock Installer',
      version='0.1',
      author="Techsrijan",
      description='My First analog clock',
      options={'build_exe': {'include_files': include_files}},
      executables=executables)

