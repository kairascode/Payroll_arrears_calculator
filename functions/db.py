from dotenv import load_dotenv
from pathlib import Path
import os

#LOAD APP SETTINGS FROM THE .ENV FILE
env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

def getAllowances():
    with open(os.getenv("FILLCOMBO"),'r') as reader:
        ress=reader.read()

        return ress

