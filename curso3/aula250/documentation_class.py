"""Este é um módulo de exemplo
Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""

class Foo:
    """Este é um módulo de exemplo
    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.z = None

    def soma(self, x: int | float, y: int | float) -> int | float:
        """
        Soma x e y
        Este módulo contém funções e exemplos de documentação de funções.
        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float
        :return: A soma entre x e y
        :rtype: int or float
        """
        return self.x + self.y

    def multiplica(
        self,
        x: int | float,
        y: int | float,
        z: int | float | None = None
    ) -> int | float:
        """Multiplica x, y e/ou z
        Multiplica x e y. Se z for enviado, multiplica x, y, z.
        """
        if self.z is None:
            return self.x * self.y
        return self.x * self.y * self.z
