from matrix import Matrix
from kivy.metrics import dp
from datetime import datetime
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import SlideTransition

class Pythagor_table(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app

        self.current_date = datetime.now().strftime("%d %B, %Y")
        self.orientation = 'vertical'

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Pythagor table', color='black', font_size=25)
        self.date = Label(text=f'Current date: {self.current_date}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(self.date)

        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(datetime.now().month), 
            year=datetime.now().year
        )
        
        self.table = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.95, 0.5),
            column_data=[('', dp(5))] + [(str(i), dp(5)) for i in range(1,31)],
            rows_num=12,
            row_data=matx.get_month_matrix(),
        )

        individual = Button(text="Individual matrix")
        individual.bind(on_press=self.individual_button)

        input = Button(text="Input data", pos =(20, 20))
        input.bind(on_press=self.input_button)

        potential = Button(text="Potential graph", pos =(20, 20))
        potential.bind(on_press=self.potential_button)
        
        buttons = BoxLayout(padding=8, size_hint=(1, 0.08))
        buttons.add_widget(individual)
        buttons.add_widget(input)
        buttons.add_widget(potential)

        self.add_widget(header)
        self.add_widget(self.table)
        self.add_widget(buttons)
    
    def individual_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'right')
        self.__app.screen_manager.current = 'individual_matrix'

    def input_button(self, item):
        date = MDDatePicker()
        date.bind(on_save=self.update_date)
        date.open()

    def potential_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'potential_graph'

    def update_date(self, instance, value, date_range):
        date: datetime = value
        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(date.month), 
            year=date.year
        )

        self.date.text = f'Current date: {date.strftime("%d %B, %Y")}'
        self.table.row_data = matx.get_month_matrix()