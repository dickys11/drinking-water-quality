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
        if a == b:
            self.x = [b, c, d]
            self.y = [1, 1, 0]
        elif c == d:
            self.x = [a, b, c]
            self.y = [0, 1, 1]
        else:
            self.x = [a, b, c, d]
            self.y = [0, 1, 1, 0]

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

    def get_coor_x(self):
        return self.x

    def get_coor_y(self):
        return self.y


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


def input_value():
    # inisialisasi input
    ph = {}
    do = {}
    tds = {}

    ph['low'] = Trapezoid(0, 0, 5, 6)
    ph['mid'] = Trapezoid(5, 6, 9, 10)
    ph['hi'] = Trapezoid(9, 10, 14, 14)

    do['low'] = Trapezoid(0, 0, 3, 3.5)
    do['mid'] = Trapezoid(3, 3.5, 4.5, 5)
    do['hi'] = Trapezoid(4.5, 5, 10, 10)

    tds['low'] = Trapezoid(0, 0, 50, 70)
    tds['mid'] = Trapezoid(50, 70, 180, 200)
    tds['hi'] = Trapezoid(180, 200, 300, 300)

    return ph, do, tds


def fuzzification(ph, do, tds, input_ph, input_do, input_tds):
    ph_membership = {}
    do_membership = {}
    tds_membership = {}

    ph_membership['low'] = ph['low'].membership(input_ph)
    ph_membership['mid'] = ph['mid'].membership(input_ph)
    ph_membership['hi'] = ph['hi'].membership(input_ph)

    do_membership['low'] = do['low'].membership(input_do)
    do_membership['mid'] = do['mid'].membership(input_do)
    do_membership['hi'] = do['hi'].membership(input_do)

    tds_membership['low'] = tds['low'].membership(input_tds)
    tds_membership['mid'] = tds['mid'].membership(input_tds)
    tds_membership['hi'] = tds['hi'].membership(input_tds)

    return ph_membership, do_membership, tds_membership


def inference(ph_membership, do_membership, tds_membership):
    cond_membership = {}
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

    cond_membership['bad'] = max(bad_cond)
    cond_membership['good'] = max(good_cond)
    return cond_membership


def output_value():
    cond = {}
    cond['bad'] = Trapezoid(0, 0, 40, 60)
    cond['good'] = Trapezoid(40, 60, 100, 100)
    return cond


def defuzzification(cond, cond_membership):
    # cond_bad = Trapezoid(0, 0, 40, 60)
    # cond_good = Trapezoid(40, 60, 100, 100)

    # print('bad')
    # print('good')
    num = 0
    den = 0
    for i in range(10, 101, 10):
        value = np.fmax(cond['bad'].output(cond_membership['bad'], i),
                        cond['good'].output(cond_membership['good'], i))
        num += i*value
        den += value

    final_value = num/den
    # print(round(final_value, 2))
    return final_value


def showgraph(ph, do, tds, cond):
    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4)
    ax0.plot(ph['low'].get_coor_x(), ph['low'].get_coor_y(), 'r', label="low")
    ax0.plot(ph['mid'].get_coor_x(), ph['mid'].get_coor_y(), 'g', label="mid")
    ax0.plot(ph['hi'].get_coor_x(), ph['hi'].get_coor_y(), 'y', label="hi")
    ax0.set_title('pH')
    ax0.legend()

    ax1.plot(do['low'].get_coor_x(), do['low'].get_coor_y(), 'r', label="low")
    ax1.plot(do['mid'].get_coor_x(), do['mid'].get_coor_y(), 'g', label="mid")
    ax1.plot(do['hi'].get_coor_x(), do['hi'].get_coor_y(), 'y', label="hi")
    ax1.set_title('DO')
    ax1.legend()

    ax2.plot(tds['low'].get_coor_x(),
             tds['low'].get_coor_y(), 'r', label="low")
    ax2.plot(tds['mid'].get_coor_x(),
             tds['mid'].get_coor_y(), 'g', label="mid")
    ax2.plot(tds['hi'].get_coor_x(), do['hi'].get_coor_y(), 'y', label="hi")
    ax2.set_title('TDS')
    ax2.legend()

    ax3.plot(cond['bad'].get_coor_x(),
             cond['bad'].get_coor_y(), 'r', label="bad")
    ax3.plot(cond['good'].get_coor_x(),
             cond['good'].get_coor_y(), 'g', label="good")
    ax3.set_title('Condition')
    ax3.legend()

    for ax in (ax0, ax1, ax2, ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    plt.tight_layout()
    plt.show()
