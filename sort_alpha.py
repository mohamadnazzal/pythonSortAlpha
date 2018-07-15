

print "Wait.."

bands = list()

filename = 'Names_sorted.txt'
with open (filename) as fin:
    for line in fin:
        bands.append(line.strip())

bands.sort()

filename = 'names_sorted_final.txt'
with open(filename, 'w') as fout:
    for band in bands:
        fout.write(band + '\n')

print "done"
