from os import stat
from hurry.filesize import size

def file_uploader(file_path, file_name):
    file_size = get_file_size(file_path + file_name)
    if (_is_file_too_large(file_size)):
        return "Max file size is 50M - your file is too large: size(file_size)"


    print ("file_size: %s" % file_size)

def _get_file_size(file):
    file_stats = stat(file)
    return file_stats.st_size

def _is_file_too_large(file_size):
    if file_size > 50000000:
        return True
    return False

def _split_file_needed(file_size):
    if file_size > 13295377:
        return True
    return False

def split_file(file_path, filename):
    NUM_OF_LINES=5000

    with open(file_path + filename) as fin:
        # output_filename = "%s_0.txt"%(filename, "w")
        fout = open(file_path + "split/%s_0.txt/"%(filename), "w")
        for i,line in enumerate(fin):
          fout.write(line)
          if (i+1)%NUM_OF_LINES == 0:
            fout.close()
            fout = open(file_path + "split/%s_%d.txt"%(filename, i/NUM_OF_LINES+1),"w")
        fout.close()
