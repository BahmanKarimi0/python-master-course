import sys
import tempfile
import os
import shutil


class TempDir:
    def __init__(self, dir=None, dir_prefix='temp_', file_prefix='temp_', file_suffix='.txt', delete=True):
        self.base_dir = dir
        self.dir_prefix = dir_prefix
        self.file_prefix = file_prefix
        self.file_suffix = file_suffix
        self.delete = delete
        self.temp_dir_name = None
        self.temp_file_name = None
        if self.base_dir:
            os.makedirs(self.base_dir, exist_ok=True)

    def __enter__(self):
        self.temp_dir_name = tempfile.mkdtemp(dir=self.base_dir, prefix=self.dir_prefix)
        fd, self.temp_file_name = tempfile.mkstemp(dir=self.temp_dir_name, prefix=self.file_prefix,
                                                   suffix=self.file_suffix)
        os.close(fd)
        return self.temp_dir_name, self.temp_file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.delete and self.temp_dir_name and os.path.exists(self.temp_dir_name):
            try:
                shutil.rmtree(self.temp_dir_name)
            except Exception as e:
                print("Warning: could not delete temporary directory.", e, file=sys.stderr)


with TempDir(delete=False) as (temp_dir, temp_file):
    print("Temporary directory created:", temp_dir)
    print("*" * 40)
    with open(temp_file, 'w+') as f:
        f.write("Hello World")
        f.seek(0)
        print(f.read())
