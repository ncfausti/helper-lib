import subprocess

def getClipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboard(data):
     p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
     p.stdin.write(data)
     p.stdin.close()
     retcode = p.wait()

def transposeAndCopy(dataIds):
    col = ''
    ids = dataIds.split()
    for i in range(len(ids)):
        col+=ids[i]+'\n'
    setClipboard(col)
    return col
