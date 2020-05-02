import os
from pyats.easypy import run
from genie import testbed
#from genie.harness.main import gRun

def main(runtime):
   
    run(testscript = os.path.join('./topology_test.py'), testbed=testbed.load(os.path.join('./default_testbed.yaml')))