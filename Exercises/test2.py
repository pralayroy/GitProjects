#a1@QH.com, b1@QH.com
#Replace QH by gmail
with open('a.txt', 'rt') as ws:
    with open('b.txt', 'wt') as re:
        for line in ws:
          re.write(line.replace('QH', 'gmail'))


