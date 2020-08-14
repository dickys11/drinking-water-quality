import sys
import function
from gui import Ui_MainWindow
from PyQt5 import QtWidgets


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_calc.clicked.connect(self.calculatePressed)
        self.pushButton_showgraph.clicked.connect(self.showGraph)

    def calculatePressed(self):
        ph, do, tds = self.getInput()
        phF, doF, tdsF = function.input_value()
        ph_membership, do_membership, tds_membership = function.fuzzification(
            phF, doF, tdsF, ph, do, tds)

        # print(ph_membership)
        # print(do_membership)
        # print(tds_membership)
        self.memberLabel_ph_low.setText(
            str(ph_membership['low']))
        self.memberLabel_ph_mid.setText(
            str(ph_membership['mid']))
        self.memberLabel_ph_high.setText(
            str(ph_membership['hi']))

        self.memberLabel_do_low.setText(
            str(do_membership['low']))
        self.memberLabel_do_mid.setText(
            str(do_membership['mid']))
        self.memberLabel_do_high.setText(
            str(do_membership['hi']))

        self.memberLabel_tds_low.setText(
            str(tds_membership['low']))
        self.memberLabel_tds_mid.setText(
            str(tds_membership['mid']))
        self.memberLabel_tds_high.setText(
            str(tds_membership['hi']))

        cond_membership = function.inference(
            ph_membership, do_membership, tds_membership)

        doF = function.output_value()

        final_value = function.defuzzification(doF, cond_membership)
        self.label_condition.setText(f'{str(round(final_value, 2))}/100')

    def getInput(self):
        self.inputPH = self.doubleSpinBox_ph.value()
        self.inputDO = self.doubleSpinBox_do.value()
        self.inputTDS = self.doubleSpinBox_tds.value()
        return (self.inputPH, self.inputDO, self.inputTDS)

    def showGraph(self):
        phF, doF, tdsF = function.input_value()
        condF = function.output_value()
        function.showgraph(phF, doF, tdsF, condF)


def main():
    app = QtWidgets.QApplication(sys.argv)
    fuzz = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
