# encoding: utf-8
import gzip
import os
import sys

"""
    EXAMPLE:
        python some/very/long/path/directory_with_chunks
    RETURNS:
        directory_with_chunks.json.gz
"""

dir_name = sys.argv[1]

##dir_name=os.getcwd()+'/'

print(dir_name)

item_counter, line_counter = 0, 0

destination = './' +  dir_name.split('/')[-1] + '.json.gz'

print(destination)

with gzip.open(destination, 'w') as f:
    f.write('{ "tweets": [')

    for fname in os.listdir(sys.argv[1]):
        if fname == '.DS_Store':
            item_counter += 1
        else:
            print 'Formatting item ' + str(item_counter) + ', file: ' + fname

            cfile = gzip.open(sys.argv[1] + '/' + fname, 'rb')

            for line in cfile.readlines():
                if item_counter < len(os.listdir(sys.argv[1])) - 1:
                    f.write(line.replace('}\n', '},\n'))
                else:
                    if line_counter < 499:
                        f.write(line.replace('}\n', '},\n'))
                        line_counter += 1
                    else:
                        f.write(line)

            item_counter += 1

    f.write(']}')