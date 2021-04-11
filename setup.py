import sys
from src.index import run
from os import environ
with open('./.env') as env:
  for line in env:
    keyValueList = line.split('=')
    if(len(keyValueList)>1):
      environ[keyValueList[0]] = keyValueList[1]


if __name__ == "__main__":
    if(sys.argv[1] == 'run'):
        run()