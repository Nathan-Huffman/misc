#---------------------------------------------
# Params.py
# Nathan Huffman
# Combines params from file and command line
#---------------------------------------------

#---Parameters-----------------
epochs = 1000
learning_rate = 0.01
experiment = 'Baby_00'

config_file = 'test_json.json'

#---Imports-----------------
import argparse
import json

# Handle arguments via JSON
def handle_args_JSON(): 
    config = argparse.ArgumentParser(add_help=False)
    config.add_argument('--config', help='Configuration file', default=config_file)
    
    parser = argparse.ArgumentParser(parents=[config])
    parser.add_argument('--epochs', type=int, help='Number of epochs to train', default=epochs)
    parser.add_argument('--ex', type=int, help='Number of epochs to train', default=epochs)
    parser.add_argument('-l', '--learn_rate', type=int, help='Number of epochs to train', default=learning_rate)
    parser.add_argument('-s', '--supercomputer', action='store_true', help='Flag to run on supercomputer')
    parser.add_argument('-e', '--eval', action='store_true', help='Flag run as evaluation')
    
    args, unknown = config.parse_known_args()
    
    if args.config is not None:
        json_dict = json.load(open(args.config))
        vars(args).update(json_dict)
        
    parser.parse_args(unknown, args)
    
    return args

print(handle_args_JSON())