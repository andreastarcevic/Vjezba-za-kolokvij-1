class pogadanjebrojaError(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: 'ERROR-000: Nespecificirana pogreška',
            101: 'ERROR-101: Uneseni broj je izvan traženog raspona',
        }
        try:
            self.error_message += self.error_dict[code] 
        except KeyError:
            self.error_message += self.error_dict[000]