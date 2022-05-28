from datetime import datetime

class Config:
    def __init__(self) -> None:
        self.current_date = datetime.now().strftime("%d %B, %Y")