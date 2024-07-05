# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# type: ignore

# new = ''
# for j in range(5):
#     text_ = input(':')
#     new += text_
#     try:
#         float(new)
#         print(new)
#     except ValueError:
#         print('Not included')
#         new = new[:-1]
#     print(new)

# i = input(':')
# j = float(i)
# print(j)

# s = ''
# b = bool(s)
# f = float(s)
# print(b, f)

class Test:
    def __init__(self, text) -> None:
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


suitcase = Test('banana')
print(suitcase.text)
suitcase.text = 'apple'
print(suitcase.text)
