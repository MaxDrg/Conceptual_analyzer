from datetime import datetime
from kivymd.app import MDApp
from data_manager import Date
from pythagor import Pythagor_table
from potential import Potential_graph
from individual import Individual_matrix
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config 
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '550')
Config.set('graphics','resizable', False)
Config.write()

class ConceptualAnalyzerApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        screen = Screen(name='pythagor_table')
        self.pythagor = Pythagor_table(app)
        screen.add_widget(self.pythagor)
        self.screen_manager.add_widget(screen)

        screen = Screen(name='individual_matrix')
        self.individual = Individual_matrix(app)
        screen.add_widget(self.individual)
        self.screen_manager.add_widget(screen)

        screen = Screen(name='potential_graph')
        self.potential = Potential_graph(app)
        screen.add_widget(self.potential)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    date = Date()
    date.set_date()
    app = ConceptualAnalyzerApp()
    app.run()