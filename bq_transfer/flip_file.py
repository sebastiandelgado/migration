import sys

path = sys.argv[1]
new_path = sys.argv[2]

origin_file = open(path, "r")

class front_appender:
    def __init__(self, fname, mode='w'):
        self.__f = open(fname, mode)
        self.__write_queue = []

    def write(self, s):
        self.__write_queue.insert(0, s)

    def close(self):
        self.__f.writelines(self.__write_queue)
        self.__f.close()

f = front_appender(new_path)
line = origin_file.readline()
while line:
	f.write(line)
	line = origin_file.readline()
f.close()