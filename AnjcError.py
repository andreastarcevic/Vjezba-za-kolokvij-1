class AnjcError(Exception):
	def __init__(self, code = 000):
		self.errorMessage = None

		self.errorDict = {
			000 : "Error 000 : Nespecificirani error",
			101 : "Error 101 : Krivi unos u glavnom meniju",
			102 : "Error 102 : Krivi unos u meniju povlačenja karata"
		}

		try:
			self.errorMessage = self.errorDict[code]
		except KeyError:
			self.errorMessage = self.errorDict[000]

		print("\n")
		print("=" * 75)
		print(self.errorMessage)
		print("=" * 75)
		print("\n")