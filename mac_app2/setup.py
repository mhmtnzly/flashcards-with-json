from setuptools import setup
import py2app

APP=['display.py']
Options={'argv_emulation':True,}
DATA_FILES=['english.json']

setup(app=APP, 
data_files=DATA_FILES,
options={'py2app':Options,},
setup_requires=['py2app'],
)
