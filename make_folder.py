import os

# make result folder
if 'test' in os.listdir(os.getcwd()): pass
else: os.mkdir('./test')
