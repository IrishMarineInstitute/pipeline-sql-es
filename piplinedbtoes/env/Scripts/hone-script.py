#!C:\Users\girwin\Source\Repos\IrishMarineInstitute\pipeline-sql-es\piplinedbtoes\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hone==0.1.4','console_scripts','hone'
__requires__ = 'hone==0.1.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hone==0.1.4', 'console_scripts', 'hone')()
    )
