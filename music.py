import os
from difflib import SequenceMatcher

path = r"C:\Users\micha\Music"

def similar_fNames(fname1, fname2):
    name1 = fname1.split('.')[0]
    name2 = fname2.split('.')[0]
    similarity = SequenceMatcher(None, name1, name2).ratio()
    return similarity

def delete_duplicates_in_dir(path, to_skip = []):
    last_file = ''
    count = 0
    # print(path)
    for file in os.listdir(path):
        f = os.path.join(path, file)
        # print(file)
        if file in to_skip:
            continue
        if os.path.isdir(f):
            print(f, end = '\t')
            delete_duplicates_in_dir(f)
            continue
        if similar_fNames(file, last_file) > 0.6:
            print(file,'\t', last_file)
            toRemove = os.path.join(path, file)
            # print(toRemove, os.path.isdir(toRemove))
            os.remove(toRemove)
            count = count + 1
            last_file = file
    print(f'{count}/{len(os.listdir(path))} similar files deleted')
        
delete_duplicates_in_dir(path)
