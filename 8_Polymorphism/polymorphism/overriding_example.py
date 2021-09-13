class Country:
    def capital(self):
        print("Country has a capital")


    def language(self):
        print("country has a language")


class SriLanka(Country):
    def capital(self):
        print("Colombo is the capital of Sri Lanka")

    def language(self):
        print("Sinhala is the main language")


country = Country()
srilanka = SriLanka()

country.capital()
srilanka.capital()



