#!/usr/bin/python
import os
import subprocess

# Change directory
path = 'C:\\Working\\STM\\Unit_Tests\\DMI\\dmi-etcs_interface\\Module_Tests'
os.chdir(path)

# Make inc-file with a cygwin shell
#subprocess.call("C:/cygwin/bin/bash.exe C:/Working/STM_Tools/Tools/prj2inc.bash")


# Wake the server
for i in range(0, 2):
	print('\n \n --------------------------- \n Waking server \n ~brought to you by the awesome Tove  \n --------------------------- \n')
	subprocess.call(['ati'])
	
print('\n \n --------------------------- \n Generating code coverage \n ~brought to you by the awesome Tove \n --------------------------- \n')

# Generate code coverage
subprocess.call(['C:\\Working\\STM\\Unit_Tests\\DMI\\dmi-etcs_interface\\Module_Tests\\Generate_All_Test_results.bat'])

# This is a comment
# That you will likely ignore
# Also, a haiku


