from pathlib import Path
from tokenize import String

data = Path("./data")


str_fmt = "Case #{}: {}"

def casePrint(i, val, end='\n'):
    print(str_fmt.format(i + 1, val), end=end)

def get_read_write(filename: str, val: bool):
    if val:
        return input, casePrint

    filepath = data / filename
    file = filepath.open("r")

    ofilename = filepath.stem + "output.txt"
    ofilepath = data / ofilename
    ofile = ofilepath.open("w+")

    def read():
        return file.readline().strip()

    def write(i, val, end='\n'):
        return ofile.write(str_fmt.format(i + 1, val) + end)

    return read, write
