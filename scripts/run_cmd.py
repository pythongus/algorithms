from subprocess import run, Popen, PIPE

pwd = Popen(["pwd"], stdout=PIPE)
ret = Popen(["ls", "-lh"], stdin=pwd.stdout, stdout=PIPE)
pwd.stdout.close()

breakpoint()
output = ret.communicate()[0]
print(output)
