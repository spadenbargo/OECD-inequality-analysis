import sys
fname = sys.argv[1]
# delim = sys.argv[2]
f = open(fname, "r")
f_str = f.read()
f.close()
# lines = [line for line in f_str.split('\n') if line != delim]
lines = [line for line in f_str.split('\n')]

res = []
curr_str = ''

for i in range(len(lines)):
    if (i + 1) % 4 == 0:
        curr_str += lines[i] + '\n'
    else:
        curr_str += lines[i]


fw = open(f"{fname.replace('.csv', '')}-cleaned.csv", "w")
fw.write(curr_str)
fw.close()