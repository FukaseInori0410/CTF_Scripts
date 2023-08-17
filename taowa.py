import gzip
import os
import tarfile
import zipfile
import re
import py7zr

# 解压.tar.gz
def untar(fname):
    t = tarfile.open(fname)
    t.extractall('bao/')

# 解压.zip
def unzip(fname):
    z = zipfile.ZipFile(fname)
    z.extractall('bao/')

# 解压.7z
def un7z(fname):
    z = py7zr.SevenZipFile(fname)
    z.extractall('bao/')

for i in range(9749):
    file_name = os.listdir('bao')[0]
    file_name_without_ext = re.findall(r'^(\w+)\.', file_name)[0]
    file_extension = file_name.replace(file_name_without_ext, '', 1)
    if file_extension == '.tar.gz':
        untar('bao/' + file_name)
    elif file_extension == '.zip':
        unzip('bao/' + file_name)
    elif file_extension == '.7z':
        un7z('bao/' + file_name)
    os.remove('bao/' + file_name)

