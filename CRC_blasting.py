import zipfile
import string
from binascii import crc32

printable_str = string.printable
blast_str = ""

for i in range(0, 68):
    zip_name = "b2ca8799-13d7-45df-a707-94373bf2800c/" + "out" + str(i) + ".zip"
    z = zipfile.ZipFile(zip_name, "r")
    crc = z.getinfo("data.txt").CRC  # 十进制crc
    for a in printable_str:
        for b in printable_str:
            for c in printable_str:
                for d in printable_str:
                    temp_str = a+b+c+d
                    if crc32(temp_str.encode()) == crc:
                        blast_str += temp_str
                        print(blast_str)
