import json
from config import Config
from datetime import datetime

cfg = Config()

class Date:
    def get_date(self):
        with open(cfg.date_filename, "r") as json_data:
            return json.load(json_data)

    def set_date(self, year = datetime.now().year, 
                        month = datetime.now().month, 
                        day = datetime.now().day):
        date = datetime(year=year, month=month, day=day).strftime("%d %B, %Y")
        
        data: dict = self.get_date()
        new_data = { "current_date": date }
        data.update(new_data)

        with open(cfg.date_filename, "w") as json_data:
            json.dump(data, json_data, indent=2)