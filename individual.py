from config import Config
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import SlideTransition

cfg = Config()

class Individual_matrix(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app

        self.orientation = 'vertical'
        # view = BoxLayout(orientation = 'vertical')

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Individual matrix', color='black', font_size=25)
        date = Label(text=f'Current date: {cfg.current_date}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(date)
        
        table = MDDataTable(
            # name column, width column, sorting function column(optional)
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.95, 0.5),
            column_data=[(str(i), dp(30)) for i in range(1,5)],
            row_data=[
                ("2", "1", "2", "3", "6"),
                ("2", "1", "2", "3", "6"),
                ("3", "1", "2", "3", "6"),
                ("3", "1", "2", "3", "6"),
            ],
        )

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
        self.add_widget(table)
        self.add_widget(buttons)
    
    def pythagor_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'pythagor_table'

    def input_button(self, item):
        date = MDDatePicker()
        date.open()

    def potential_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'right')
        self.__app.screen_manager.current = 'potential_graph'