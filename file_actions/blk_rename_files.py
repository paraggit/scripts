""" 
This script will rename or move files form the given location.

usages:
    blk_rename_file.py -s/--sourcedir <dir_path>  [-d/--destinationdir] <destination_dir> 

"""
import os
import argparse
import string
import random
import sys

def get_random_string(length=13):
    """ Generate random string.
        
        :param:
            [length] : random string length
        :return:
            random string
    """
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_random_name(filename):
    """ Generate random filename but preserve its extension.
        :param:
            filename: name of file
        :return:
            random file name
    """
    name, extension = os.path.splitext(filename)
    newname = get_random_string()

    if name.startswith('.'):
        newname = '.'+newname

    if (name == '') and (extension == ''):
        return False

    elif (extension == ''):
        return newname
    else:
        return newname+extension
        

def run(sdir, ddir, verbos=False):
    """ This main function to run the file rename logic.

        :param:
            sdir : Source Dir
            ddir: Destination Dir.
        :return:
            exitcode 0 On successful execution.
            exitcode 1,2,3 on failure.
    """
    if not os.path.isdir(sdir):
        print("Source dir is not exists")
        sys.exit(1)

    # walking through all directory Path.
    for root, dirs, files in os.walk(sdir, topdown=True):
        for name in files:
            flpath = os.path.join(root, name)
            dirname = os.path.dirname(flpath)
            flname = os.path.basename(flpath)
            newname = generate_random_name(flname)

            if ddir is None:
                dest_path = "{}/{}".format(dirname,newname)
            else:
                dest_dir = "{}/{}".format(ddir,dirname)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                dest_path = "{}/{}".format(dest_dir, newname)

            if verbos:
                print("SRC:"+ flpath +"DEST:"+ dest_path)
            os.rename(flpath, dest_path)

    return 0

if __name__ == "__main__":
    # construct Argument 
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-s", "--sourcedir", required=True, help="Source Dir")
    ap.add_argument("-d", "--destinationdir", required=False, help="Destination Dir")
    
    args = vars(ap.parse_args())
    sdir = args['sourcedir']
    ddir = args['destinationdir']

    run(sdir, ddir, verbos=True)
