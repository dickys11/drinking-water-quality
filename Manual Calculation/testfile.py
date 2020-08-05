import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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

    def get_coor_x(self):
        return self.x

    def get_coor_y(self):
        return self.y


ph_low = Trapezoid(0, 0, 5, 6)
ph_mid = Trapezoid(5, 6, 9, 10)
ph_hi = Trapezoid(9, 10, 14, 14)

fig, (ax0) = plt.subplots(nrows=3)
ax0.plot(ph_low.get_coor_x(), ph_low.get_coor_y(), 'r', label="low")
ax0.plot(ph_mid.get_coor_x(), ph_mid.get_coor_y(), 'g', label="mid")
ax0.plot(ph_hi.get_coor_x(), ph_hi.get_coor_y(), 'y', label="hi")
ax0.legend()

ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.get_xaxis().tick_bottom()
ax0.get_yaxis().tick_left()
plt.show()
