import os

def clear_temp_files(files):
    for f in files:
        try:
            os.unlink(f)
        except:
            pass

        