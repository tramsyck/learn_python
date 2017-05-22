import time
def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

logfile = open('access-log')
loglines = follow(logfile)
pylines = grep('python', loglines)

for line in pylines:
    print(line,)
