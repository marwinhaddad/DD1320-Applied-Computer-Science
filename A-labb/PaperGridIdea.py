import sys

n = int(sys.stdin.readline())
nlist = [int(x) for x in sys.stdin.readline().split()]
cur_p = 1
next_p = 1
tejp_sum = 0
long_l = (1/(2**(3/4)))
kort_l = (1/(2**(5/4)))

area_A1 = long_l * kort_l * 2
total_area = 0

for x in nlist:
    total_area += long_l * kort_l * x
    long_l, kort_l = kort_l, long_l/2
if area_A1 > total_area or sum(nlist) > 10**9:
    print('impossible')
    exit()

long_l = (1/(2**(3/4)))
kort_l = (1/(2**(5/4)))
total_area = 0

for paper in nlist:
    next_p += 1
    if paper != 0:
        total_area += long_l * kort_l * paper
        if (next_p - cur_p) % 2 == 0:
            antal_kol = 2 ** ((next_p - cur_p)/2)
            antal_rad = antal_kol
        else:
            antal_kol = 2**(((next_p+1) - cur_p)/2)
            antal_rad = antal_kol/2
        slots = antal_kol * antal_rad
        if next_p % 2 == 0:
            tejp_sum += (antal_kol-1) * antal_rad * long_l  # +  antal_kol * (antal_rad-1) * kort_l
        else:
            tejp_sum += (antal_kol-1) * antal_rad * long_l # + antal_kol * (antal_rad-1) * kort_l
        if paper == slots or area_A1 < total_area:
            break
        elif paper < slots:
            cur_p = next_p
    kort_l, long_l = long_l/2, kort_l
print(tejp_sum)
