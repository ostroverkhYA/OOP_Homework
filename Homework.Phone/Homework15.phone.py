class Phones:
    _phone1 = 123
    _calls1 = 0
    _phone2 = 321
    _calls2 = 0
    _phone3 = 444
    _calls3 = 0

    def get_calls(self, num):
        if num == self._phone1:
            self._calls1 += 1
            print("Call in progres")
            print("received calls", self._calls1)
        if num == self._phone2:
            self._calls2 += 1
            print("Call in progres")
            print("received calls", self._calls2)
        if num == self._phone3:
            self._calls3 += 1
            print("Call in progres")
            print("received calls", self._calls3)
        else:
            print('Wrong number')


Vera = Phones()

Vera.get_calls(123)
Vera.get_calls(123)
Vera.get_calls(321)
Vera.get_calls(321)
Vera.get_calls(321)
Vera.get_calls(444)
Vera.get_calls(554)
