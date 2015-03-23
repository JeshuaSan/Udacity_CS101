# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(size, size_unit, bw, bw_unit):
    table = {'k': 2 ** 10,
             'M': 2 ** 20,
             'G': 2 ** 30,
             'T': 2 ** 40,
             'B': 8,
             'b': 1}
    bits = size  * table[size_unit[0]] * table[size_unit[1]] * 1.0
    bits_per_s = bw * table[bw_unit[0]] * table[bw_unit[1]] * 1.0
    seconds = bits / bits_per_s
    return convert_seconds(seconds)

def convert_seconds(seconds):
    hours = int(seconds / 3600.0)
    minutes = int((seconds % 3600.0) / 60.0)
    seconds = (seconds % 60.0) % 60.0
    if seconds % 1.0 != 0:
        pass
    else:
        seconds = int(seconds)
    names = [['hour',hours],['minute',minutes],['second',seconds]]
    for name in names:
        if name[1] != 1:
            name[0] +=  's'
    return '{} {}, {} {}, {} {}'\
            .format(names[0][1], names[0][0],
                    names[1][1], names[1][0],
                    names[2][1], names[2][0])

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(13,'GB', 1, 'MB')
#>>> 3 hours, 41 minutes, 52 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
