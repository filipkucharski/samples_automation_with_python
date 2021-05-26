#!/usr/bin/env python3
import sys
import os
import re
import glob


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  if os.path.isdir(log_file):
   print('Processing directory...')
   log_files = [f for f in listdir_fullpath(log_file) if os.path.isfile(os.path.join(log_file,f))]
   for log_file in log_files:
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
         error_patterns = []
         for i in range(len(error.split(' '))):
            error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
         if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
            returned_errors.append(log)
        file.close()
   return returned_errors
  else:
    print('Processing one log file...')
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
         error_patterns = ["info"]
         for i in range(len(error.split(' '))):
            error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
         if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
            returned_errors.append(log)
        file.close()
    return returned_errors
  
def file_output(returned_errors):
  output_path = input('Where do you want to save the output? ')
  with open(output_path.strip('"') + '\errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
    
    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)