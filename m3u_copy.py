import os.path
import shutil
import sys


def m3u_copy(source, destination):
    try:
        file = open(source).readlines()
    except IOError:
        print("Cannot open m3u file")
        return
    if not os.path.exists(destination) or not os.path.isdir(destination):
        print("No such destination directory or destination is not a directory")
        return
    if "/" in source:
        source_path = source[:source.rindex("/")+1]
    else:
        source_path = ""
    shutil.copy(source, destination)
    for line in file:
        if line.strip() != '':
            line = line[:len(line) - 1]
            if "/" in line and not os.path.exists(destination + line[:line.rindex("/") + 1]):
                os.makedirs(destination + line[:line.rindex("/") + 1])
            if not os.path.isfile(source_path + line):
                print(f"{line} does not exist")
            else:
                try:
                    shutil.copy(source_path + line, destination + line)
                except IOError:
                    print(f"{line} cannot be copied, function terminated")
                    return


def main():
    m3u_copy(sys.argv[1], sys.argv[2])
    return 0


if __name__ == '__main__':
    sys.exit(main())
