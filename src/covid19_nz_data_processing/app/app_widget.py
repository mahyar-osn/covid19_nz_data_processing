from PyQt4 import QtGui

from src.covid19_nz_data_processing.app.ui_plot_app import Ui_MainWindow
from src.covid19_nz_data_processing.main import Basic


class PlotWidget(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._run_data = Basic()

        self._make_connections()
        self.showNormal()

    def _make_connections(self):
        self._ui.open.clicked.connect(self._plot)
        self._ui.export_2.clicked.connect(self._export)

    def _plot(self):
        self._run_data.plot_daily_trend()
        self._run_data.plot_cumulative_sum()
        self._run_data.plot_daily_arrival_sum()
        self._run_data.plot_overseas_date_reported()

    def _export(self):
        folder = str(QtGui.QFileDialog.getExistingDirectory(self, "Select directory to save the files"))

        if not folder:
            QtGui.QMessageBox.warning(self, 'No directory selected', 'Please select a valid directory')
            return

        self._run_data.export_data(self._run_data._total_combined, folder+'/combined_sum.csv')
        self._run_data.export_data(self._run_data._grand_sum, folder+'/cumulative_sum.csv')
        self._run_data.export_data(self._run_data._total_arrival, folder+'/daily_arrival_sum.csv')
        self._run_data.export_data(self._run_data._total_overseas_reported_date, folder+'/overseas_reported_sum.csv')

        msg = QtGui.QMessageBox()
        msg.setWindowTitle("Files saved!")
        msg.setText("All files saved!")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        result = msg.exec_()
        return
