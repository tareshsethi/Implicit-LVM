import sys
import os
import pathlib

from glob import glob
from os import makedirs, path, remove, rmdir
from stm import parse_stm_file

stm_dirs = ['data/train_stm', 'data/val_stm', 'data/test_stm']

for stm_dir in  stm_dirs:
    dir_new = stm_dir.split('_')[0] + '_txt/'
    os.makedirs(dir_new)

    for stm_file in glob(path.join(stm_dir, "*.stm")):

        # Parse stm file
        stm_segments = parse_stm_file(stm_file)
        transcripts = []

        for stm_segment in stm_segments:
            transcripts.append(stm_segment.transcript + '\n')

        # create new file
        txt_file_name = dir_new + pathlib.Path(stm_file).name.split('.')[0] + '.txt'
        with open (txt_file_name, 'w') as f:
            f.writelines(transcripts)