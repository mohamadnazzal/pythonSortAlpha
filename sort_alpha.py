

print "Wait.."

words = list()

filename = 'words.txt'
with open (filename) as fin:
    for line in fin:
        words.append(line.strip())

words.sort()

filename = 'words_sorted_done.txt'
with open(filename, 'w') as fout:
    for word in words:
        fout.write(word + '\n')

print "done"
