import sys, os
sys.path.append(os.path.abspath('../'))
from el_core.SingleTon import SingleTon
class UA:
  @staticmethod
  def getLang():
    lang = {}
    # Головна
    lang['main'] = 'Пошук шляху'
    lang['main_radio_dijkstra'] = 'Дейкстри'
    lang['main_radio_astar'] = 'А* (А стар)'
    lang['main_start'] = 'Перейти'
    # Дейкстра
    lang['dijkstra_main'] = 'Дейкстра'
    lang['dijkstra_tab'] = 'Головна'
    lang['dijkstra_tab_2'] = 'Результат роботи'
    lang['dijkstra_l_number'] = 'Кількість точок:'
    lang['dijkstra_l_m_number'] = 'Кількість зєднань:'
    lang['dijkstra_l_start'] = 'Початкова точка:'
    lang['dijkstra_generated'] = 'Генерувати'
    lang['dijkstra_go'] = 'Виконати'

    lang['dijkstra_row'] = 'Вершина {}'
    lang['dijkstra_summ'] = 'Сума'

    lang['dijkstra_error_merge_column'] = 'Дані не в межах від 1 до {}'
    lang['dijkstra_error_table'] = 'Не всі дані занесено в таблицю! Нижче поля!'
    lang['dijkstra_error'] = 'Помилка'
    lang['dijkstra_error_no_all_data'] = 'Ви заповнили не всі дані'
    lang['dijkstra_error_no_all_data_detalis'] = "Поля: кількість точок, кількість з'єднань, початкова точка мають бути заповнені!"
    lang['dijkstra_error_data_not_int'] = 'Дані не цілочисельного типу'

    lang['dijkstra_log_input'] = 'Вхідні дані:'
    lang['dijkstra_log_output'] = 'Вихідні дані:'
    lang['dijkstra_log_passage'] = 'Дані проходження:'
    lang['dijkstra_log_best_ways'] = 'Найкращі шляхи з вершини {}:'
    # А* (А стар)
    lang['astar_main'] = 'A* (A стар)'
    lang['astar_row_text'] = 'Рядків'
    lang['astar_column_text'] = 'Стовпців'
    lang['astar_start_text'] = 'Точка початку'
    lang['astar_end_text'] = 'Точка кінця'
    lang['astar_info_text'] = 'Введіть дані, тільки числа і символ # як перегорода'
    lang['astar_generate'] = 'Генерувати'
    lang['astar_go'] = 'Виконати'
    return lang

class US:
  @staticmethod
  def getLang():
    lang = {}
    # Main
    lang['main'] = 'Path searching'
    lang['main_radio_dijkstra'] = 'Dijkstra'
    lang['main_radio_astar'] = 'A* (А star)'
    lang['main_start'] = 'Go'
    # Dijkstra
    lang['dijkstra_main'] = 'Dijkstra'
    lang['dijkstra_tab'] = 'Home'
    lang['dijkstra_tab_2'] = 'The result of work'
    lang['dijkstra_l_number'] = 'Number of points:'
    lang['dijkstra_l_m_number'] = 'Number of connections:'
    lang['dijkstra_l_start'] = 'Starting point:'
    lang['dijkstra_generated'] = 'Generate'
    lang['dijkstra_go'] = 'Perform'

    lang['dijkstra_row'] = 'Top {}'
    lang['dijkstra_summ'] = 'Sum'

    lang['dijkstra_error_merge_column'] = 'Data is not in range from 1 to {}'
    lang['dijkstra_error_table'] = 'Not all data is listed! Below the field!'
    lang['dijkstra_error'] = 'Error'
    lang['dijkstra_error_no_all_data'] = 'You did not fill out all data'
    lang['dijkstra_error_no_all_data_detalis'] = 'Fields: the number of points, the number of connections, the starting point must be filled!'
    lang['dijkstra_error_data_not_int'] = 'Data is not an integer type'

    lang['dijkstra_log_input'] = 'Incoming data:'
    lang['dijkstra_log_output'] = 'Output data:'
    lang['dijkstra_log_passage'] = 'Passage data:'
    lang['dijkstra_log_best_ways'] = 'The best paths from the top {}:'
    # А* (А стар)
    lang['astar_main'] = 'A* (A star)'
    lang['astar_row_text'] = 'Row'
    lang['astar_column_text'] = 'Columns'
    lang['astar_start_text'] = 'Start point'
    lang['astar_end_text'] = 'End point'
    lang['astar_info_text'] = 'Enter data, only numbers and the # character as a partition'
    lang['astar_generate'] = 'Generate'
    lang['astar_go'] = 'Perform'
    return lang

@SingleTon
class Lang:
    @property
    def language(self):
        if self.__session_lang == 'us':
            self.__lang = US
        elif self.__session_lang == 'ua':
            self.__lang = UA
        else:
            raise RuntimeError('Language error: Language not found`s')
        return self.__lang.getLang()

    @language.setter
    def language(self, lang):
        if type(lang) is str:
            if lang == 'us':
                self.__session_lang = 'us'
            elif lang == 'ua':
                self.__session_lang = 'ua'
            else:
                raise RuntimeError('Language error: Language not found`s')
        else:
            raise RuntimeError('Language error: Lang is not str')