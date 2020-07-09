import cx_Freeze
import sys
import selenium
base=None
if(sys.platform=='win32'):
	base="Win32GUI"
executables=[cx_Freeze.Executable("AutonomousUMS.py",base=base,icon='logo.ico')]

cx_Freeze.setup(name='AutonomousUMS',
				options={"build_exe":{"packages":["tkinter","selenium"]}},
				version='0.1',
				description="Save those 30 seconds with AutonomousUMS",
				executables=executables)