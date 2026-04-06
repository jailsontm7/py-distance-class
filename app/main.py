class Distance:
    class Distance:
        def __init__(self, km):
            self.km = km

        def __str__(self):
            return f"Distance: {self.km} kilometers."

        def __repr__(self):
            return f"Distance(km={self.km})"

        def __add__(self, other):
            # Verifica se estamos somando com outro objeto Distance ou com um número
            value = other.km if isinstance(other, Distance) else other
            return Distance(self.km + value)

        def __iadd__(self, other):
            # Implementa o operador +=
            value = other.km if isinstance(other, Distance) else other
            self.km += value
            return self

        def __mul__(self, other):
            # Multiplicação (geralmente por um número escalar)
            return Distance(self.km * other)

        def __truediv__(self, other):
            # Divisão com arredondamento de 2 casas decimais
            result = self.km / other
            return Distance(round(result, 2))

        # Métodos de Comparação
        # Criamos uma função auxiliar para extrair o valor de 'other'
        # para evitar repetição de código
        def _get_value(self, other):
            return other.km if isinstance(other, Distance) else other

        def __lt__(self, other):
            return self.km < self._get_value(other)

        def __gt__(self, other):
            return self.km > self._get_value(other)

        def __eq__(self, other):
            return self.km == self._get_value(other)

        def __le__(self, other):
            return self.km <= self._get_value(other)

        def __ge__(self, other):
            return self.km >= self._get_value(other)
