from virl2_client import ClientLibrary 
from pyats.topology import loader
import yaml
import argparse

parser = argparse.ArgumentParser(description='Get testbed file from CML lab')
parser.add_argument('hostname', metavar='-H', type=str, help='CML host')
parser.add_argument('username', metavar='-u', type=str, help='CML username')
parser.add_argument('password', metavar='-p', type=str, help='CML password')
parser.add_argument('lab', metavar='-l', type=str, help='CML lab id')
parser.add_argument('output', metavar='-o', type=str, help='output file')
args = parser.parse_args()

client_library = ClientLibrary("https://" + args.hostname, args.username, 
                               args.password, ssl_verify=False)
lab = client_library.join_existing_lab(args.lab)
testbed_yaml = lab.get_pyats_testbed()
with open(args.output, 'w') as file:
    documents = yaml.dump(yaml.safe_load(testbed_yaml), file)