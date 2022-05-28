from config import Config
from kivy.uix.button import Button
from kivymd.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDDatePicker
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.screenmanager import SlideTransition

cfg = Config()

class Potential_graph(BoxLayout):
    def __init__(self, app):
        super().__init__()
        self.__app = app

        self.orientation = 'vertical'

        header = BoxLayout(size_hint=(1, 0.06))

        title = Label(text='Potential graph', color='black', font_size=25)
        date = Label(text=f'Current date: {cfg.current_date}', color='black', font_size=25)
        
        header.add_widget(title)
        header.add_widget(date)

        graph_buttons = BoxLayout(padding=8, size_hint=(1, 0.08))
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
            # xlabel='X', ylabel='Y', 
            #size_hint=(1, 0.5),
            #xlabel= "Time",
            #ylabel = "CPU Usage (%)",
            #draw_border=False,
            #x_ticks_minor=1,
            #x_ticks_major=1, 
            #y_ticks_major=1,
            #y_grid_label=True, 
            #x_grid_label=True, 
            #padding=10,
            #x_grid=True, 
            #y_grid=True, 
            #xmin=0, xmax=30, ymin=0, ymax=13,
        )
        #graph = Graph(y_ticks_major=0.5,
        #    #x_ticks_major=64,
        #    size_hint=(0.93, 0.2),
        #    border_color=[0, 1, 1, 1],
        #    tick_color=[0, 1, 1, 0.7],
        #    x_grid=True, y_grid=True,
        #    xmin=0, xmax=30,
        #    ymin=0, ymax=13,
        #    draw_border=True,
        #    x_grid_label=True, y_grid_label=True
        #)

        plot = MeshLinePlot(color=[1, 0, 0, 10])
        plot.points = [(x, 0.5 + x) if x % 2 == 0 and x <= 12 else (x, 0.5) for x in range(0, 30)]
        graph.add_plot(plot)

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
        date.open()

    def individual_button(self, item):
        self.__app.screen_manager.transition = SlideTransition(direction = 'left')
        self.__app.screen_manager.current = 'individual_matrix'

    def get_graph(self, item):
        pass