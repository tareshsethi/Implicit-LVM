from glob import glob

txt_dirs = ['train_txt', 'val_txt', 'test_txt']

for txt_dir in txt_dirs:

    read_files = glob(txt_dir + "/" + "*.txt")
    outfile_name = txt_dir.split("_")[0] + ".txt"
    with open(outfile_name, "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())