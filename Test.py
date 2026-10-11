class

def set_current_date(self):
    now = datetime.now()
    current_date = str(now).split()
    self.current_date = current_date[0]