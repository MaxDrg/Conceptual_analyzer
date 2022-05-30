from matrix import Matrix
from datetime import datetime
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.screenmanager import SlideTransition

class Potential_graph(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app
        
        self.current_date = datetime.now().strftime("%d %B, %Y")
        self.orientation = 'vertical'

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Potential graph', color='black', font_size=25)
        self.date = Label(text=f'Current date: {self.current_date}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(self.date)

        graph_buttons = BoxLayout(padding=8, size_hint=(1, 0.06))
        for i in range(1, 13):
            button = Button(text=str(i), pos =(20, 20))
            button.bind(on_press=self.get_graph)
            graph_buttons.add_widget(button)
        
        graph = Graph(
            size_hint=(1, 0.5),
            xlabel= "Day",
            ylabel = "Num",
            y_ticks_major = 1,
            y_grid_label = True,
            x_grid_label = True,
            x_grid = True,
            y_grid = True,
            padding = 10,
            xmin = 0,
            xmax = 30,
            x_ticks_major = 1,
            ymin = 0,
            ymax = 13,
            background_color = [0, 0, 0, 1],
        )

        self.plot = MeshLinePlot(color=[1, 0, 0, 10])

        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(datetime.now().month), 
            year=datetime.now().year
        )
        
        self.plot.points = matx.get_num_matrix(1)
        graph.add_plot(self.plot)

        pythagor = Button(text="Pythagor table", pos =(20, 20))
        pythagor.bind(on_press=self.pythagor_button)

        input = Button(text="Input data", pos =(20, 20))
        input.bind(on_press=self.input_button)

        individual = Button(text="Individual matrix")
        individual.bind(on_press=self.individual_button)

        buttons = BoxLayout(padding=8, size_hint=(1, 0.08))
        buttons.add_widget(pythagor)
        buttons.add_widget(input)
        buttons.add_widget(individual)
        
        self.add_widget(header)
        self.add_widget(graph_buttons)
        self.add_widget(graph)
        self.add_widget(buttons)
    
    def pythagor_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'right')
        self.__app.screen_manager.current = 'pythagor_table'

    def input_button(self, item):
        date = MDDatePicker()
        date.bind(on_save=self.update_date)
        date.open()

    def individual_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'individual_matrix'

    def get_graph(self, item):
        date: datetime = datetime.strptime(self.date.text, 'Current date: %d %B, %Y')
        date_input = lambda x: x if len(str(x)) == 2 else f"0{x}"

        matx = Matrix(
            month=date_input(date.month), 
            year=date.year
        )
        self.plot.points = matx.get_num_matrix(item.text)

    def update_date(self, instance, value, date_range):
        date: datetime = value
        self.date.text = f'Current date: {date.strftime("%d %B, %Y")}'