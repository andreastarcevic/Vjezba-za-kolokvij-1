class ajncError(Exception):
    def __init__(self, code = 000):
        self.error_message = ''
        self.error_dict = {
            000: 'ERROR-000: Nespecificirana pogreška',
            101: 'ERROR-101: Pogrešan unos. Molimo unesite drugi.'
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]