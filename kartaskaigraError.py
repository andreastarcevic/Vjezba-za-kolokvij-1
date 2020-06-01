class kartaskaigraError(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: 'ERROR-000: Nespecificirana pogreška',
        }
        try:
            self.error_message += self.error_dict[code] 
        except KeyError:
            self.error_message += self.error_dict[000]