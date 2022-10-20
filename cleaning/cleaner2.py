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
# countries = [
#     'Sweden', 'Costa Rica', 'Slovenia', 'Greece', 'Turkey', 'Netherlands', 'Denmark', 'Norway', 'Poland', 'Canada', 'Hungary', 'Portugal', 'Spain', 'Czech Republic', 'Belgium', 'Lithuania', 'Israel', 'New Zealand', 'Switzerland', 'Latvia', 'Chile', 'Austria', 'Finland', 'Korea', 'Colombia', 'Iceland', 'Japan', 'Luxembourg', 'USA', 'Estonia', 'Ireland', 'Italy', 'Mexico', 'United Kingdom', 'Australia', 'Germany'
# ]
for i in range(len(lines) - 1):
    splt = lines[i].split(';')
    if len(splt) >= 5 and int(splt[3]) >= 1950:
        # print(f"{splt[0]=}")
        # type_dt = 'income' if 'National income' in splt[1] else 'GDP'
        curr_str += f"{splt[0]},{splt[2]},{splt[3]},{splt[4]}\n"

fw = open(f"{fname.replace('.csv', '')}-subset.csv", "w")
fw.write(curr_str)
fw.close()
# row
# ['Australia', '"shweal_p90p100_z_AUTop 10% | share | adults | equal split"', 'p90p100', '1896', '']
