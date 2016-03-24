#!/usr/bin/env python
import os, os.path
import subprocess

def compile(filepath):
    """ Compile the program, returns True for success or False otherwise """
    retcode = subprocess.call("/usr/bin/g++ " + filepath, shell=True)
    return retcode == 0

def test():
    """ Returns the number of correct results """
    return subprocess.call("./test.sh ./a.out", shell=True)

def get_submission(filepath):
    """ Returns the content from the submission file """
    with open(filepath, 'r') as fs:
        text = fs.read()
    return text

def clean_up(filepath=None):
    """ Clean up files """
    subprocess.call("rm -f ./a.out", shell=True)
    if filepath:
        subprocess.call("rm -f " + filepath, shell=True)

def test_submission(filepath):
    """ Compile, test, cleanup, and return results in a dictionary """
    results = {"compiled": False, "score": 0, "has_file": False, "text": ""}
    
    # Exit if no file
    results["has_file"] = os.path.isfile(filepath)
    if not results["has_file"]:
        clean_up()
        return results
    
    # Get text submission
    results["text"] = get_submission(filepath)
    
    # Compile
    results["compiled"] = compile(filepath)
    if not compile(filepath):
        clean_up(filepath)
        return results
    
    # Test
    results["score"] = test()
    
    # Clean up
    clean_up(filepath)
    
    # Return results
    return results
