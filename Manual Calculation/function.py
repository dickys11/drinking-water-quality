import matplotlib.pyplot as plt
import numpy as np


class Trapezoid:
    """
    Kelas representasi nilai fuzzy dengan bentuk grafik trapesium
    """

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def membership(self, x):
        """
        Fungsi untuk mencari nilai keanggotaan dari sebuah input

        x = input nilai crisp
        """
        if self.b <= x <= self.c:
            return 1
        elif self.a < x < self.b:
            return round(float((x-self.a)/(self.b-self.a)), 2)
        elif self.c < x < self.d:
            return round(float((self.d-x)/(self.d-self.c)), 2)
        else:
            return 0

    def output(self, membership_value, i):
        if self.a < self.b and self.a != self.b:
            membership_axb = round(
                float(membership_value * (self.b - self.a) + self.a), 2)
            membership_dxc = None
        elif self.c < self.d and self.c != self.d:
            membership_dxc = round(
                float(-(membership_value * (self.d - self.c) - self.d)), 2)
            membership_axb = None

        # print(membership_axb)
        # print(membership_dxc)

        if membership_axb != None:
            b = membership_axb
        else:
            b = self.b
        if membership_dxc != None:
            c = membership_dxc
        else:
            c = self.c

        if b <= i <= c:
            # print('1')
            pass
        elif self.a < i < b:
            # print('2')
            membership_value = round(float((i-self.a)/(self.b-self.a)), 2)
        elif c < i < self.d:
            # print('3')
            membership_value = round(float((self.d-i)/(self.d-self.c)), 2)
        else:
            membership_value = 0

        return membership_value


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


def fuzzification(input_ph, input_do, input_tds):
    # inisialisasi input
    ph_low = Trapezoid(0, 0, 5, 6)
    ph_mid = Trapezoid(5, 6, 9, 10)
    ph_hi = Trapezoid(9, 10, 14, 14)

    do_low = Trapezoid(0, 0, 3, 3.5)
    do_mid = Trapezoid(3, 3.5, 4.5, 5)
    do_hi = Trapezoid(4.5, 5, 10, 10)

    tds_low = Trapezoid(0, 0, 50, 70)
    tds_mid = Trapezoid(50, 70, 180, 200)
    tds_hi = Trapezoid(180, 200, 300, 300)

    ph_membership = {}
    do_membership = {}
    tds_membership = {}

    ph_membership['low'] = ph_low.membership(input_ph)
    ph_membership['mid'] = ph_mid.membership(input_ph)
    ph_membership['hi'] = ph_hi.membership(input_ph)

    do_membership['low'] = do_low.membership(input_do)
    do_membership['mid'] = do_mid.membership(input_do)
    do_membership['hi'] = do_hi.membership(input_do)

    tds_membership['low'] = tds_low.membership(input_tds)
    tds_membership['mid'] = tds_mid.membership(input_tds)
    tds_membership['hi'] = tds_hi.membership(input_tds)

    return ph_membership, do_membership, tds_membership


def inference(ph_membership, do_membership, tds_membership):
    cond = {}
    bad_cond = []
    good_cond = []
    # Rules
    # Hasilnya bad
    bad_cond.append(min(tds_membership['low'],
                        do_membership['low'], ph_membership['low']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['low'], ph_membership['mid']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['low'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['mid'], ph_membership['low']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['mid'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['hi'], ph_membership['low']))
    bad_cond.append(min(tds_membership['low'],
                        do_membership['hi'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['low'], ph_membership['low']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['low'], ph_membership['mid']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['low'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['mid'], ph_membership['low']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['mid'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['hi'], ph_membership['low']))
    bad_cond.append(min(tds_membership['mid'],
                        do_membership['hi'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['low'], ph_membership['low']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['low'], ph_membership['mid']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['low'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['mid'], ph_membership['low']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['mid'], ph_membership['mid']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['mid'], ph_membership['hi']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['hi'], ph_membership['low']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['hi'], ph_membership['mid']))
    bad_cond.append(min(tds_membership['hi'],
                        do_membership['hi'], ph_membership['hi']))

    # Hasilnya good
    good_cond.append(
        min(tds_membership['low'], do_membership['mid'], ph_membership['mid']))
    good_cond.append(
        min(tds_membership['low'], do_membership['hi'], ph_membership['mid']))
    good_cond.append(
        min(tds_membership['mid'], do_membership['mid'], ph_membership['mid']))
    good_cond.append(
        min(tds_membership['mid'], do_membership['hi'], ph_membership['mid']))

    cond['bad'] = max(bad_cond)
    cond['good'] = max(good_cond)
    return cond


def defuzzification(cond_membership):
    cond_bad = Trapezoid(0, 0, 40, 60)
    cond_good = Trapezoid(40, 60, 100, 100)

    # print('bad')
    # print('good')
    num = 0
    den = 0
    for i in range(10, 101, 10):
        value = np.fmax(cond_bad.output(cond_membership['bad'], i),
                        cond_good.output(cond_membership['good'], i))
        num += i*value
        den += value

    final_value = num/den
    # print(round(final_value, 2))
    return final_value
