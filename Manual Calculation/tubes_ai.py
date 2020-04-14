import matplotlib.pyplot as plt
import numpy as np


class Trapesium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def hitung(self, x):
        if self.b <= x <= self.c:
            return 1
        elif self.a < x < self.b:
            return round(float((x-self.a)/(self.b-self.a)), 2)
        elif self.c < x < self.d:
            return round(float((self.d-x)/(self.d-self.c)), 2)
        else:
            return 0


class Output:
    def __init__(self, a, b, c, d, y):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.y = y

    def hitung_turun(self, x, nilai_baru):
        if self.b <= x <= nilai_baru:
            # print('1')
            return self.y
        elif self.a < x < self.b:
            # print('2')
            return round(float((x-self.a)/(self.b-self.a)), 2)
        elif nilai_baru < x < self.d:
            # print('3')
            return round(float((self.d-x)/(self.d-self.c)), 2)
        else:
            return 0

    def hitung_naik(self, x, nilai_baru):
        if nilai_baru <= x <= self.c:
            # print('1')
            return self.y
        elif self.a < x < nilai_baru:
            # print('2')
            return round(float((x-self.a)/(self.b-self.a)), 2)
        elif self.c < x < self.d:
            # print('3')
            return round(float((self.d-x)/(self.d-self.c)), 2)
        else:
            return 0


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0],
             line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1],
             line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div


ph_low = Trapesium(0, 0, 5, 6)
ph_mid = Trapesium(5, 6, 9, 10)
ph_hi = Trapesium(9, 10, 14, 14)

do_low = Trapesium(0, 0, 3, 3.5)
do_mid = Trapesium(3, 3.5, 4.5, 5)
do_hi = Trapesium(4.5, 5, 10, 10)

tds_low = Trapesium(0, 0, 50, 70)
tds_mid = Trapesium(50, 70, 180, 200)
tds_hi = Trapesium(180, 200, 300, 300)

cond_bad = Trapesium(0, 0, 40, 60)
cond_good = Trapesium(40, 60, 100, 100)

input_ph = 5.2
input_do = 3.22
input_tds = 52.6

ph_lvl_low = ph_low.hitung(input_ph)
ph_lvl_mid = ph_mid.hitung(input_ph)
ph_lvl_hi = ph_hi.hitung(input_ph)

do_lvl_low = do_low.hitung(input_do)
do_lvl_mid = do_mid.hitung(input_do)
do_lvl_hi = do_hi.hitung(input_do)

tds_lvl_low = tds_low.hitung(input_tds)
tds_lvl_mid = tds_mid.hitung(input_tds)
tds_lvl_hi = tds_hi.hitung(input_tds)

# bad
rule1 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_low))
rule2 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_mid))
rule3 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_hi))
rule4 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_low))
rule6 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_hi))
rule7 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_low))
rule9 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_hi))
rule10 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_low))
rule11 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_mid))
rule12 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_hi))
rule13 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_low))
rule15 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_hi))
rule16 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_low))
rule18 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_hi))
rule19 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_low))
rule20 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_mid))
rule21 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_hi))
rule22 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_low))
rule23 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_mid))
rule24 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_hi))
rule25 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_low))
rule26 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_mid))
rule27 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_hi))

cond_lvl_bad = np.fmax(rule1,
                       np.fmax(rule2,
                               np.fmax(rule3,
                                       np.fmax(rule4,
                                               np.fmax(rule6,
                                                       np.fmax(rule7,
                                                               np.fmax(rule9,
                                                                       np.fmax(rule10,
                                                                               np.fmax(rule11,
                                                                                       np.fmax(rule12,
                                                                                               np.fmax(rule13,
                                                                                                       np.fmax(rule15,
                                                                                                               np.fmax(rule16,
                                                                                                                       np.fmax(rule18,
                                                                                                                               np.fmax(rule19,
                                                                                                                                       np.fmax(rule20,
                                                                                                                                               np.fmax(rule21,
                                                                                                                                                       np.fmax(rule22,
                                                                                                                                                               np.fmax(rule23,
                                                                                                                                                                       np.fmax(rule24,
                                                                                                                                                                               np.fmax(rule25,
                                                                                                                                                                                       np.fmax(rule26, rule27
                                                                                                                                                                                               ))))))))))))))))))))))

# good
rule5 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_mid))
rule8 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_mid))
rule14 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_mid))
rule17 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_mid))


cond_lvl_good = np.fmax(rule5,
                        np.fmax(rule8,
                                np.fmax(rule14, rule17
                                        )))

# print(cond_lvl_bad)
# print(cond_lvl_good)

A = (40, 1)
B = (60, 0)
C = (40, 0)
D = (60, 1)


def cari_x_naik(y, a, b):
    x = round(float(y*(b-a)+a), 2)
    return x


def cari_x_turun(y, c, d):
    x = round(float(-(y*(d-c)-d)), 2)
    return x


x_bad_baru = cari_x_turun(cond_lvl_bad, 40, 60)
x_good_baru = cari_x_naik(cond_lvl_good, 40, 60)

cond_bad_output = Output(0, 0, 40, 60, cond_lvl_bad)
cond_good_output = Output(40, 60, 100, 100, cond_lvl_good)
num = 0
den = 0

for i in range(10, 101, 10):
    bad = cond_bad_output.hitung_turun(i, x_bad_baru)
    good = cond_good_output.hitung_naik(i, x_good_baru)
    nilai = np.fmax(bad, good)
    # print(f"{i} = {nilai}")
    num += i*nilai
    den += nilai

# print(num)
# print(round(den, 2))
nilai_akhir = num/den
print(round(nilai_akhir, 2))
