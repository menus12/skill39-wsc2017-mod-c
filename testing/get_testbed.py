from virl2_client import ClientLibrary 
from pyats.topology import loader
import yaml
import argparse
import os
   
def get_testbed(lab, host, user, passwd):
    client_library = ClientLibrary("https://" + host, user, passwd, ssl_verify=False)
    lab = client_library.join_existing_lab(args.lab)
    return lab.get_pyats_testbed()
        
    
parser = argparse.ArgumentParser(description='Get testbed file from CML lab')
parser.add_argument('--host', type=str, help='CML host (default from env)')
parser.add_argument('--user', type=str, help='CML username (default from env)')
parser.add_argument('--passwd', type=str, help='CML password (default from env)')
parser.add_argument('--lab', type=str, help='CML lab id')
parser.add_argument('--out', type=str, help='output file (default testbed.yaml)')
args = parser.parse_args()

if args.host == None:
    args.host = os.environ['CML_HOST']
if args.user == None:
    args.user = os.environ['CML_USER']
if args.passwd == None:
    args.passwd = os.environ['CML_PASS']
if args.out == None:
    args.out = 'testbed.yaml'

if args.host == None or args.user == None or args.passwd == None or args.lab == None or args.out == None:
    print (parser.print_help())
    exit(1)

tb = get_testbed(lab = args.lab, host = args.host, user = args.user, passwd = args.passwd)
with open(args.out, 'w') as file:
    documents = yaml.dump(yaml.safe_load(tb), file)
