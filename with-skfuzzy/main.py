import sys
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from gui import Ui_MainWindow
from PyQt5 import QtWidgets


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # connect buttons
        self.pushButton_calc.clicked.connect(self.calculate_pressed)

    # fuzzification process

    def fuzzification(self):
        # define universe variables
        self.input_ph = np.arange(0, 14.1, 0.1)
        self.input_do = np.arange(0, 10.1, 0.1)
        self.input_tds = np.arange(0, 301, 1)

        self.output_cond = np.arange(0, 101, 1)

        # fuzzy membership functions
        self.ph_low = fuzz.trapmf(self.input_ph, [0, 0, 5, 6])
        self.ph_mid = fuzz.trapmf(self.input_ph, [5, 6, 9, 10])
        self.ph_hi = fuzz.trapmf(self.input_ph, [9, 10, 14, 14])

        self.do_low = fuzz.trapmf(self.input_do, [0, 0, 3, 3.5])
        self.do_mid = fuzz.trapmf(self.input_do, [3, 3.5, 4.5, 5])
        self.do_hi = fuzz.trapmf(self.input_do, [4.5, 5, 10, 10])

        self.tds_low = fuzz.trapmf(self.input_tds, [0, 0, 50, 70])
        self.tds_mid = fuzz.trapmf(self.input_tds, [50, 70, 180, 200])
        self.tds_hi = fuzz.trapmf(self.input_tds, [180, 200, 300, 300])

        self.cond_bad = fuzz.trapmf(self.output_cond, [0, 0, 40, 60])
        self.cond_good = fuzz.trapmf(self.output_cond, [40, 60, 100, 100])

        # input
        self.ph = self.doubleSpinBox_ph.value()
        self.do = self.doubleSpinBox_do.value()
        self.tds = self.doubleSpinBox_tds.value()

        # calculate the membership value of the input
        self.ph_lvl_low = fuzz.interp_membership(
            self.input_ph, self.ph_low, self.ph)
        self.ph_lvl_mid = fuzz.interp_membership(
            self.input_ph, self.ph_mid, self.ph)
        self.ph_lvl_hi = fuzz.interp_membership(
            self.input_ph, self.ph_hi, self.ph)

        self.do_lvl_low = fuzz.interp_membership(
            self.input_do, self.do_low, self.do)
        self.do_lvl_mid = fuzz.interp_membership(
            self.input_do, self.do_mid, self.do)
        self.do_lvl_hi = fuzz.interp_membership(
            self.input_do, self.do_hi, self.do)

        self.tds_lvl_low = fuzz.interp_membership(
            self.input_tds, self.tds_low, self.tds)
        self.tds_lvl_mid = fuzz.interp_membership(
            self.input_tds, self.tds_mid, self.tds)
        self.tds_lvl_hi = fuzz.interp_membership(
            self.input_tds, self.tds_hi, self.tds)

        # rules
        # bad
        rule1 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_low, self.ph_lvl_low))
        rule2 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_low, self.ph_lvl_mid))
        rule3 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_low, self.ph_lvl_hi))
        rule4 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_mid, self.ph_lvl_low))
        rule6 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_mid, self.ph_lvl_hi))
        rule7 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_hi, self.ph_lvl_low))
        rule9 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_hi, self.ph_lvl_hi))
        rule10 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_low, self.ph_lvl_low))
        rule11 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_low, self.ph_lvl_mid))
        rule12 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_low, self.ph_lvl_hi))
        rule13 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_mid, self.ph_lvl_low))
        rule15 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_mid, self.ph_lvl_hi))
        rule16 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_hi, self.ph_lvl_low))
        rule18 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_hi, self.ph_lvl_hi))
        rule19 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_low, self.ph_lvl_low))
        rule20 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_low, self.ph_lvl_mid))
        rule21 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_low, self.ph_lvl_hi))
        rule22 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_mid, self.ph_lvl_low))
        rule23 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_mid, self.ph_lvl_mid))
        rule24 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_mid, self.ph_lvl_hi))
        rule25 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_hi, self.ph_lvl_low))
        rule26 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_hi, self.ph_lvl_mid))
        rule27 = np.fmin(self.tds_lvl_hi, np.fmin(
            self.do_lvl_hi, self.ph_lvl_hi))

        activation_cond_bad = np.fmin(self.cond_bad,
                                      np.fmax(rule1,
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
                                                                                                                                                                                                                      )))))))))))))))))))))))

        # good
        rule5 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_mid, self.ph_lvl_mid))
        rule8 = np.fmin(self.tds_lvl_low, np.fmin(
            self.do_lvl_hi, self.ph_lvl_mid))
        rule14 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_mid, self.ph_lvl_mid))
        rule17 = np.fmin(self.tds_lvl_mid, np.fmin(
            self.do_lvl_hi, self.ph_lvl_mid))

        activation_cond_good = np.fmin(self.cond_good,
                                       np.fmax(rule5,
                                               np.fmax(rule8,
                                                       np.fmax(rule14, rule17
                                                               ))))

        cond0 = np.zeros_like(self.output_cond)

        aggregated = np.fmax(activation_cond_bad, activation_cond_good)

        condition = fuzz.defuzz(self.output_cond, aggregated, 'centroid')

        self.cond_lvl_bad = fuzz.interp_membership(
            self.output_cond, self.cond_bad, condition)
        self.cond_lvl_good = fuzz.interp_membership(
            self.output_cond, self.cond_good, condition)

        if self.cond_lvl_bad >= self.cond_lvl_good:
            status = 'Bad'
        else:
            status = "Good"

        return (condition, status)

    def calculate_pressed(self):
        condition, status = self.fuzzification()
        condition_rounded = round(condition, 2)
        self.label_condition.setText(
            "{} ({}/100)".format(status, str(condition_rounded)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    drink = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
