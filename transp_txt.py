import re

filename = 'Judas Priest - Breaking The Law.txt'
transpose = -2

re_note = re.compile('([:\*]) (\d+) (\d+) (\d+)(.*$)')

with open(filename) as f:
  for line in f:
    res_match = re_note.match(line)
    if res_match == None:
        print line,
    else:
        pre = res_match.group(1)
        time = res_match.group(2)
        dur = res_match.group(3)
        pitch = res_match.group(4)
        rest = res_match.group(5)

        p = int(pitch)
        new_p = p + transpose
        print '%s %s %s %d%s' % (pre, time, dur, new_p, rest)
