from matrix import Matrix
from kivy.metrics import dp
from datetime import datetime
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import SlideTransition

class Individual_matrix(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app

        self.current_date = datetime.now().strftime("%d %B, %Y")
        self.orientation = 'vertical'

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Individual matrix', color='black', font_size=25)
        self.date = Label(text=f'Current date: {self.current_date}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(self.date)

        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(datetime.now().month), 
            year=datetime.now().year, 
            day=date_input(datetime.now().day)
        )

        last_nums_matx = matx.get_line_matrix()
        last_nums = f'({last_nums_matx[-2]} {last_nums_matx[-1]})'
        
        self.table = MDDataTable(
            # name column, width column, sorting function column(optional)
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.95, 0.5),
            column_data=[('', dp(37)) for i in range(1,5)],
            row_data=matx.get_matrix(),
        )

        last_nums_matx.pop(-2)
        last_nums_matx.pop(-1)

        line_matx = ''
        for num in last_nums_matx:
            line_matx += f'{num} '

        self.line_matx = Label(text=line_matx + last_nums, color='black', font_size=25, size_hint=(1, 0.08))

        potential = Button(text="Potential graph")
        potential.bind(on_press=self.potential_button)

        input = Button(text="Input data", pos =(20, 20))
        input.bind(on_press=self.input_button)

        pythagor = Button(text="Pythagor table", pos =(20, 20))
        pythagor.bind(on_press=self.pythagor_button)

        buttons = BoxLayout(padding=8, size_hint=(1, 0.08))
        buttons.add_widget(potential)
        buttons.add_widget(input)
        buttons.add_widget(pythagor)

        self.add_widget(header)
        self.add_widget(self.table)
        self.add_widget(self.line_matx)
        self.add_widget(buttons)
    
    def pythagor_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'pythagor_table'

    def input_button(self, item):
        date = MDDatePicker()
        date.bind(on_save=self.update_date)
        date.open()

    def potential_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'right')
        self.__app.screen_manager.current = 'potential_graph'

    def update_date(self, instance, value, date_range):
        date: datetime = value
        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(date.month), 
            year=date.year, 
            day=date_input(date.day)
        )
        
        last_nums_matx = matx.get_line_matrix()
        line_matx = ''
        last_nums = f'({last_nums_matx[-2]} {last_nums_matx[-1]})'

        self.date.text = f'Current date: {date.strftime("%d %B, %Y")}'
        self.table.row_data = matx.get_matrix()

        last_nums_matx.pop(-2)
        last_nums_matx.pop(-1)

        for num in last_nums_matx:
            line_matx += f'{num} '
        self.line_matx.text = line_matx + last_nums
        