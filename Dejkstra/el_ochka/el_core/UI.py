import sys, os
sys.path.append(os.path.abspath('../'))
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from el_lang.lang import Lang
from el_core.Error import HandleError
from el_core.algorithms import Dijkstra, Draw, Astar, GridWithWeights

class Ui_Dijkstra(QtWidgets.QDialog):
    """
    The class that is responsible for the window of 
    the operation of the algorithm of the action
    """
    def __init__(self):
        """
        Initializes the graphics file, creates the 
        necessary components, and causes the 
        connectors to buttons and strings...
        """
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
        """
        The method sets the language for the elements
        """
        self.setWindowTitle(Lang().language['dijkstra_main'])
        self.dijkstra_l_number.setText(Lang().language['dijkstra_l_number'])
        self.dijkstra_l_m_number.setText(Lang().language['dijkstra_l_m_number'])
        self.dijkstra_l_start.setText(Lang().language['dijkstra_l_start'])
        self.dijkstra_generated.setText(Lang().language['dijkstra_generated'])
        self.dijkstra_go.setText(Lang().language['dijkstra_go'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), Lang().language['dijkstra_tab'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), Lang().language['dijkstra_tab_2'])

    def _handlesetconnections(self):
        """
        The method establishes a connection for 
        buttons, edits, and class methods
        """
        self.dijkstra_go.setEnabled(False)
        self.dijkstra_connectors_table.setEnabled(False)
        self.dijkstra_connectors_table.cellChanged.connect(self._handleTableChange)
        self.dijkstra_generated.clicked.connect(self._handlegenerate)
        self.dijkstra_i_number.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_i_m_number.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_i_start.textChanged.connect(self._handleonlyintvalue)
        self.dijkstra_go.clicked.connect(self._handleGo)

    def _handleonlyintvalue(self):
        """
        The method checks whether 
        integer-variable variables are where 
        it is needed
        """
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
            if not 0 <= int(self.dijkstra_i_start.text()) <= int(self.dijkstra_i_number.text()) and self.dijkstra_i_start.text() != '0':
            	self.dijkstra_i_start.setText('1')
        except ValueError:
            self.dijkstra_i_start.setText('0')
            HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_l_start'] + ' ' + Lang().language['dijkstra_error_data_not_int'], '', '')
        self.dijkstra_connectors_table.setEnabled(False)
        self.dijkstra_go.setEnabled(False)

    def _handleTableChange(self, row, column):
        """
        The method is called when the parameter 
        changes in the table in the column, 
        and checks the data
        """
        try:
            if column == 2:
                float(self.dijkstra_connectors_table.item(row, column).text())
            else:
                if not 1 <= int(self.dijkstra_connectors_table.item(row, column).text()) <= int(self.dijkstra_i_number.text()):
                    self.dijkstra_connectors_table.item(row, column).setText("1")
                    HandleError(Lang().language['dijkstra_error'], Lang().language['dijkstra_error_merge_column'].format(self.dijkstra_i_number.text()), '', '')
        except ValueError:
            self.dijkstra_connectors_table.item(row, column).setText("1")

    @QtCore.pyqtSlot()
    def _handlegenerate(self):
        """
        The method invoked when a button is 
        pressed to generate, and, by the given 
        parameters, generates a table for using 
        the algorithm.
        """
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

    @QtCore.pyqtSlot()
    def _handleGo(self):
        """
        The method is called when the button is 
        pressed forward, and it starts the 
        algorithm of the Dijkstra, calculates 
        everything and sends the data to the log, 
        and then changes the tab's position to 
        the log page.
        """
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
        	try:
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
	        except MemoryError:
	        	self.dijkstra_log.clear()
	        	HandleError(Lang().language['dijkstra_error'], Lang().language['MemoryError'], '', '')


class Ui_Astar(QtWidgets.QDialog):
    """
    The class that is responsible for the window of 
    the operation of the algorithm of the action
    """
    def __init__(self):
        super().__init__()
        self.__windowsLoadet = False
        uic.loadUi('el_ui/astar.ui', self)
        self.setWindowIcon(QtGui.QIcon('el_images/main.png'))
        self._handlesetlanguage()
        self._handlesetconnections()
        self.__windowsLoadet = True
    
    def _handlesetlanguage(self):
        """
        Initializes the graphics file, creates the 
        necessary components, and causes the 
        connectors to buttons and strings...
        """
        self.setWindowTitle(Lang().language['astar_main'])
        self.astar_row_text.setText(Lang().language['astar_row_text'])
        self.astar_column_text.setText(Lang().language['astar_column_text'])
        self.astar_start_text.setText(Lang().language['astar_start_text'])
        self.astar_end_text.setText(Lang().language['astar_end_text'])
        self.astar_info_text.setText(Lang().language['astar_info_text'])
        self.astar_generated.setText(Lang().language['astar_generate'])
        self.astar_go.setText(Lang().language['astar_go'])

    def _handlesetconnections(self):
        """
        The method establishes a connection for 
        buttons, edits, and class methods and set
        base value to the text fields
        """
        self.astar_wallsandweights.cellChanged.connect(self._handleTableChange)
        self.astar_row.textChanged.connect(self._handleonlyintvalue)
        self.astar_column.textChanged.connect(self._handleonlyintvalue)
        self.astar_start_x.textChanged.connect(self._handleonlyintvalue)
        self.astar_start_y.textChanged.connect(self._handleonlyintvalue)
        self.astar_end_x.textChanged.connect(self._handleonlyintvalue)
        self.astar_end_y.textChanged.connect(self._handleonlyintvalue)
        self.astar_generated.clicked.connect(self._handlegenerate)
        self.astar_go.clicked.connect(self._handleGo)

        self.astar_row.setText('0')
        self.astar_column.setText('0')
        self.astar_start_x.setText('0')
        self.astar_start_y.setText('0')
        self.astar_end_x.setText('0')
        self.astar_end_y.setText('0')
        self.astar_wallsandweights.setEnabled(False)
        self.astar_go.setEnabled(False)


    def _handleonlyintvalue(self):
        """
        The method checks whether 
        integer-variable variables are where 
        it is needed
        """
        if not self.__windowsLoadet:
            return
        try:
            int(self.astar_row.text())
        except ValueError:
            self.astar_row.setText('0')
            HandleError(Lang().language['astar_error'], Lang().language['astar_row_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')

        try:
            int(self.astar_column.text())
        except ValueError:
            self.astar_column.setText('0')
            HandleError(Lang().language['astar_error'], Lang().language['astar_column_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')

        try:
            if not 1 <= int(self.astar_start_x.text()) <= int(self.astar_column.text()) and int(self.astar_column.text()) != 0:
                self.astar_start_x.setText('1')
        except ValueError:
            self.astar_start_x.setText('1')
            HandleError(Lang().language['astar_error'], Lang().language['astar_start_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')

        try:
            if not 1 <= int(self.astar_start_y.text()) <= int(self.astar_row.text()) and int(self.astar_row.text()) != 0:
                self.astar_start_y.setText('1')
        except ValueError:
            self.astar_start_y.setText('1')
            HandleError(Lang().language['astar_error'], Lang().language['astar_start_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')

        try:
            if not 1 <= int(self.astar_end_x.text()) <= int(self.astar_column.text()) and int(self.astar_column.text()) != 0:
                self.astar_end_x.setText('1')
        except ValueError:
            self.astar_end_x.setText('1')
            HandleError(Lang().language['astar_error'], Lang().language['astar_end_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')

        try:
            if not 1 <= int(self.astar_end_y.text()) <= int(self.astar_row.text()) and int(self.astar_row.text()) != 0:
                self.astar_end_y.setText('1')
        except ValueError:
            self.astar_end_y.setText('1')
            HandleError(Lang().language['astar_error'], Lang().language['astar_end_text'] + ' ' + Lang().language['astar_error_data_not_int'], '', '')
        self.astar_wallsandweights.setEnabled(False)
        self.astar_go.setEnabled(False)

    def _handleTableChange(self, row, column):
        """
        The method is called when the parameter 
        changes in the table in the column, 
        and checks the data
        """
        try:
            if self.astar_wallsandweights.item(row, column).text() == '#':
                pass
            else:
                int(self.astar_wallsandweights.item(row, column).text())
        except ValueError:
            self.astar_wallsandweights.item(row, column).setText("0")

    @QtCore.pyqtSlot()
    def _handlegenerate(self):
        """
        The method invoked when a button is 
        pressed to generate, and, by the given 
        parameters, generates a table for using 
        the algorithm.
        """
        self.astar_wallsandweights.setColumnCount(int(self.astar_column.text()))
        self.astar_wallsandweights.setRowCount(int(self.astar_row.text()))
        self.astar_wallsandweights.resizeColumnsToContents()
        self.astar_wallsandweights.setEnabled(True)
        self.astar_go.setEnabled(True)

    @QtCore.pyqtSlot()
    def _handleGo(self):
        """
        The method is called when the button is 
        pressed forward, and it starts the 
        algorithm of the Astar, calculates 
        everything and sends the data to the log, 
        and then changes the tab's position to 
        the log page.
        """
        walls = []
        weights = {}
        self.astar_log.clear()
        self.astar_log.appendPlainText(Lang().language['astar_input_data'])
        for row in range(self.astar_wallsandweights.rowCount()):
            temp = []
            for column in range(self.astar_wallsandweights.columnCount()):
                if self.astar_wallsandweights.item(row, column) is None:
                    walls.append((row, column))
                    temp.append('#')
                else:
                    if self.astar_wallsandweights.item(row, column).text() == '#':
                        walls.append((row, column))
                        temp.append('#')
                    else:
                        weights[(row, column)] = int(self.astar_wallsandweights.item(row, column).text())
                        temp.append(self.astar_wallsandweights.item(row, column).text())
            self.astar_log.appendPlainText('\t'.join(str(x) for x in temp))

        data = GridWithWeights(self.astar_wallsandweights.columnCount(), self.astar_wallsandweights.rowCount())
        data.walls = walls
        data.weights = weights
        start = (int(self.astar_start_x.text()) - 1, int(self.astar_start_y.text()) - 1)
        goal = (int(self.astar_end_x.text()) - 1, int(self.astar_end_y.text()) - 1)
        astar = Astar()
        came_from, cost_so_far = astar.Search(data, start, goal)
        output_str = Draw().grid(data, width=1, point_to=came_from, start=start, goal=goal)
        output_num = Draw().grid(data, width=1, number=cost_so_far, start=start, goal=goal)
        self.astar_log.appendPlainText(Lang().language['astar_paths'])
        for i in range(len(output_str)):
            self.astar_log.appendPlainText(''.join(str(x) for x in output_str[i]))

        self.astar_log.appendPlainText(Lang().language['astar_paths_number'])
        for i in range(len(output_num)):
            self.astar_log.appendPlainText(''.join(str(x) for x in output_num[i]))
        self.tabWidget.setCurrentIndex(1)


class Ui_MainWindow(QtWidgets.QMainWindow):
    """
    The class responsible for the main window of the program
    """
    def __init__(self):
        """
        The class that is responsible for the Main Widnow
        load design from the file main.ui and set based icon
        from the buttons
        """
        super().__init__()
        uic.loadUi('el_ui/main.ui', self)
        self.setWindowIcon(QtGui.QIcon('el_images/main.png'))
        self.language_ua.setIcon(QtGui.QIcon('el_images/ua.png'))
        self.language_us.setIcon(QtGui.QIcon('el_images/us.png'))
        Lang().language = 'ua'
        self.__handleConnections()

    def __handleConnections(self):
        """
        The method establishes a connection for 
        buttons, edits, and class methods
        """
        self.language_ua.clicked.connect(self._handleSetLangUA)
        self.language_us.clicked.connect(self._handleSetLangUS)
        self.main_start.clicked.connect(self._handleGo)

    def _handleSetLangUA(self):
        """
        The method use if user click from button
        lang ua, and translate program from lang
        ukrainian
        """
        Lang().language = 'ua'
        self._handlesetlang()

    def _handleSetLangUS(self):
        """
        The method use if user click from button
        lang us, and translate program from lang
        english
        """
        Lang().language = 'us'
        self._handlesetlang()

    def _handlesetlang(self):
        """
        Method change text from main widnow 
        depending on the language
        """
        self.main_radio_dijkstra.setText(Lang().language['main_radio_dijkstra'])
        self.main_radio_astar.setText(Lang().language['main_radio_astar'])
        self.main_start.setText(Lang().language['main_start'])
        self.setWindowTitle(Lang().language['main'])

    def _handleGo(self):
        """
        The method is called when the user 
        presses the forward button and 
        starts the selected algorithm
        """
        if self.main_radio_astar.isChecked():
            view = Ui_Astar()
            view.exec_()
        elif self.main_radio_dijkstra.isChecked():
            view = Ui_Dijkstra()
            view.exec_()
        else:
            raise RuntimeError('UI Error: Method not found')
