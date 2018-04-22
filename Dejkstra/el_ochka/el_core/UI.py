import sys, os
sys.path.append(os.path.abspath('../'))
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from el_lang.lang import Lang
from el_core.Error import HandleError
from el_core.algorithms import Dijkstra

class Ui_Dijkstra(QtWidgets.QDialog):
    def __init__(self):
        self.__windowsLoadet = False
        super().__init__()
        uic.loadUi('el_ui/dijkstra.ui', self)
        self.setWindowIcon(QtGui.QIcon('el_images/main.png'))
        self._handlesetlanguage()
        self._handlesetconnections()
        self.dijkstra_i_number.setText('0')
        self.dijkstra_i_m_number.setText('0')
        self.dijkstra_i_start.setText('0')
        self.__windowsLoadet = True
        self.__go = False

    def _handlesetlanguage(self):
        self.setWindowTitle(Lang().language['dijkstra_main'])
        self.dijkstra_l_number.setText(Lang().language['dijkstra_l_number'])
        self.dijkstra_l_m_number.setText(Lang().language['dijkstra_l_m_number'])
        self.dijkstra_l_start.setText(Lang().language['dijkstra_l_start'])
        self.dijkstra_generated.setText(Lang().language['dijkstra_generated'])
        self.dijkstra_go.setText(Lang().language['dijkstra_go'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), Lang().language['dijkstra_tab'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), Lang().language['dijkstra_tab_2'])

    def _handlesetconnections(self):
        self.dijkstra_go.setEnabled(False)
        self.dijkstra_connectors_table.cellChanged.connect(self._handleTableChange)
        self.dijkstra_generated.clicked.connect(self._handlegenerate)
        self.dijkstra_i_number.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_i_m_number.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_i_start.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_go.clicked.connect(self._handleGo)

    def _handleonlyintvalue(self):
        if not self.__windowsLoadet:
            return
        try:
            int(self.dijkstra_i_number.text())
        except ValueError:
            self.dijkstra_i_number.setText('0')
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_l_number'] + ' ' + Lang().language['dijkstra_error_data_not_int'], '', '')
        try:
            int(self.dijkstra_i_m_number.text())
        except ValueError:
            self.dijkstra_i_m_number.setText('0')
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_l_m_number'] + ' ' + Lang().language['dijkstra_error_data_not_int'], '', '')
        try:
            int(self.dijkstra_i_start.text())
        except ValueError:
            self.dijkstra_i_start.setText('0')
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_l_start'] + ' ' + Lang().language['dijkstra_error_data_not_int'], '', '')
        self.dijkstra_connectors_table.setEnabled(False)
        self.dijkstra_go.setEnabled(False)

    def _handleTableChange(self, row, column):
        try:
            if column == 2:
                float(self.dijkstra_connectors_table.item(row, column).text())
            else:
                if not 1 <= int(self.dijkstra_connectors_table.item(row, column).text()) <= int(self.dijkstra_i_number.text()):
                    self.dijkstra_connectors_table.item(row, column).setText("1")
                    HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_error_merge_column'].format(self.dijkstra_i_number.text()), '', '')
        except ValueError:
            self.dijkstra_connectors_table.item(row, column).setText("1")

    def _handlegenerate(self):
        if len(self.dijkstra_i_number.text()) == 0 or len(self.dijkstra_i_m_number.text()) == 0 or len(self.dijkstra_i_start.text()) == 0:
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_error_no_all_data'], Lang().language['dijkstra_error_no_all_data_detalis'], '')
        else:
            self.dijkstra_connectors_table.setColumnCount(3)
            self.dijkstra_connectors_table.setRowCount(int(self.dijkstra_i_m_number.text()))
            self.dijkstra_connectors_table.setHorizontalHeaderLabels([
                Lang().language['dijkstra_row'].format(1), 
                Lang().language['dijkstra_row'].format(2), 
                Lang().language['dijkstra_summ']
                ])
            self.dijkstra_connectors_table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignLeft)
            self.dijkstra_connectors_table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.dijkstra_connectors_table.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignRight)
            self.dijkstra_connectors_table.resizeColumnsToContents()
            self.dijkstra_connectors_table.setEnabled(True)
            self.dijkstra_go.setEnabled(True)

    def _handleGo(self):
        array = []
        error_data = "({}, {}), "
        error_message = ""
        error_count = 0
        self.dijkstra_log.clear()
        self.dijkstra_log.appendPlainText(Lang().language['dijkstra_log_input'])
        self.dijkstra_log.appendPlainText(
            Lang().language['dijkstra_row'].format(1) + '\t' +
            Lang().language['dijkstra_row'].format(2) + '\t' +
            Lang().language['dijkstra_summ']
            )
        
        for row in range(self.dijkstra_connectors_table.rowCount()):
            tarray = []
            for column in range(self.dijkstra_connectors_table.columnCount()):
                if self.dijkstra_connectors_table.item(row, column) is None:
                    error_message = error_message + error_data.format(row + 1, column + 1)
                    error_count += 1
                else:
                    tarray.append(int(self.dijkstra_connectors_table.item(row, column).text()))
            array.append(tarray)
            if error_count == 0:
                self.dijkstra_log.appendPlainText(str(tarray[0]) + '\t' + str(tarray[1]) + '\t'  + str(tarray[2]))
        if error_count > 0:
            self.dijkstra_log.clear()
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_error_table'], error_message, '')
        else:
            dijkstra = Dijkstra()
            dijkstra.algorithm = {
            'n': int(self.dijkstra_i_number.text()),
            'm': int(self.dijkstra_i_m_number.text()),
            'start': int(self.dijkstra_i_start.text()),
            'array': array
            }
            data = dijkstra.algorithm
            
            self.dijkstra_log.appendPlainText(Lang().language['dijkstra_log_output'])
            self.dijkstra_log.appendPlainText(Lang().language['dijkstra_log_passage'])
            self.dijkstra_log.appendPlainText(', '.join(str(i) for i in data['bytes']))
            self.dijkstra_log.appendPlainText(Lang().language['dijkstra_log_best_ways'].format(self.dijkstra_i_start.text()))
            for i in range(len(data['path'])):
                to_return = ' -> '.join(str(x) for x in data['path'][i + 1])
                self.dijkstra_log.appendPlainText(str(i + 1) + ": " + to_return)
            self.tabWidget.setCurrentIndex(1)

class Ui_Astar(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('el_ui/astar.ui', self)
        self.setWindowIcon(QtGui.QIcon('el_images/main.png'))
        self._handlesetlanguage()
    
    def _handlesetlanguage(self):
        self.setWindowTitle(Lang().language['astar_main'])
        self.astar_row_text.setText(Lang().language['astar_row_text'])
        self.astar_column_text.setText(Lang().language['astar_column_text'])
        self.astar_start_text.setText(Lang().language['astar_start_text'])
        self.astar_end_text.setText(Lang().language['astar_end_text'])
        self.astar_info_text.setText(Lang().language['astar_info_text'])
        self.astar_generate.setText(Lang().language['astar_generate'])
        self.astar_go.setText(Lang().language['astar_go'])
        

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('el_ui/main.ui', self)
        self.setWindowIcon(QtGui.QIcon('el_images/main.png'))
        self.language_ua.setIcon(QtGui.QIcon('el_images/ua.png'))
        self.language_us.setIcon(QtGui.QIcon('el_images/us.png'))
        Lang().language = 'ua'
        self.__handleConnections()

    def __handleConnections(self):
        self.language_ua.clicked.connect(self._handleSetLangUA)
        self.language_us.clicked.connect(self._handleSetLangUS)
        self.main_start.clicked.connect(self._handleGo)

    def _handleSetLangUA(self):
        Lang().language = 'ua'
        self._handlesetlang()

    def _handleSetLangUS(self):
        Lang().language = 'us'
        self._handlesetlang()

    def _handlesetlang(self):
        self.main_radio_dijkstra.setText(Lang().language['main_radio_dijkstra'])
        self.main_radio_astar.setText(Lang().language['main_radio_astar'])
        self.main_start.setText(Lang().language['main_start'])
        self.setWindowTitle(Lang().language['main'])

    def _handleGo(self):
        if self.main_radio_astar.isChecked():
            view = Ui_Astar()
            view.exec_()
        elif self.main_radio_dijkstra.isChecked():
            view = Ui_Dijkstra()
            view.exec_()
        else:
            raise RuntimeError('UI Error: Method not found')