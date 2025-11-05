# coding: UTF-8

class Fracao:
    """
    Classe para criar e manipular objetos do tipo fração.
    Simplifica automaticamente a fração no momento da criação.
    """

    def __init__(self, num, den):
        """
        Construtor: Chamado ao criar uma nova Fracao (ex: f = Fracao(3, 4))
        """
        if den == 0:
            # Uma fração não pode ter denominador zero
            raise ValueError("O denominador não pode ser zero.")

        self.num = num
        self.den = den

        # Padroniza o sinal: o negativo fica sempre no numerador
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

        # Simplifica a fração assim que ela é criada
        self.simplifica()

    def mdc(self):
        """
        Calcula o Máximo Divisor Comum (MDC) entre o numerador e o denominador
        usando o Algoritmo de Euclides.
        """
        x = abs(self.num)
        y = abs(self.den)
        
        while y != 0:
            x, y = y, x % y
        
        return x

    def simplifica(self):
        """
        Divide o numerador e o denominador pelo seu MDC para simplificar a fração.
        """
        divisor = self.mdc()
        if divisor > 1:
            self.num //= divisor  # Divisão inteira
            self.den //= divisor  # Divisão inteira
        return self

    def __str__(self):
        """
        Controla como a fração é impressa (ex: print(f1))
        """
        if self.num == 0:
            return "0"
        elif self.den == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.den}'

    def __add__(self, outra_fracao):
        """
        Sobrecarga do operador de soma (+). Retorna uma *nova* fração.
        (a/b) + (c/d) = (ad + bc) / (bd)
        """
        novo_num = (self.num * outra_fracao.den) + (self.den * outra_fracao.num)
        novo_den = self.den * outra_fracao.den
        
        # O construtor da nova fração irá simplificá-la automaticamente
        return Fracao(novo_num, novo_den)

    def __iadd__(self, outra_fracao):
        """
        Sobrecarga do operador de soma "em-place" (+=). Modifica a própria fração.
        """
        # Calcula o novo numerador
        self.num = (self.num * outra_fracao.den) + (self.den * outra_fracao.num)
        # Calcula o novo denominador
        self.den *= outra_fracao.den
        
        # Simplifica a fração modificada e retorna ela mesma
        return self.simplifica()

    def __sub__(self, outra_fracao):
        """
        Sobrecarga do operador de subtração (-). Retorna uma *nova* fração.
        (a/b) - (c/d) = (ad - bc) / (bd)
        """
        novo_num = (self.num * outra_fracao.den) - (self.den * outra_fracao.num)
        novo_den = self.den * outra_fracao.den
        
        return Fracao(novo_num, novo_den)
    
    def __mul__(self, outra_fracao):
        """
        Sobrecarga do operador de multiplicação (*). Retorna uma *nova* fração.
        (a/b) * (c/d) = (ac) / (bd)
        """
        novo_num = self.num * outra_fracao.num
        novo_den = self.den * outra_fracao.den
        
        return Fracao(novo_num, novo_den)
    
    def __truediv__(self, outra_fracao):
        """
        Sobrecarga do operador de divisão (/). Retorna uma *nova* fração.
        (a/b) / (c/d) = (ad) / (bc)
        """
        if outra_fracao.num == 0:
            raise ValueError("Não é possível dividir por uma fração com numerador zero.")
        
        novo_num = self.num * outra_fracao.den
        novo_den = self.den * outra_fracao.num
        
        return Fracao(novo_num, novo_den)
    
    def __eq__(self, outra_fracao):
        """
        Sobrecarga do operador de igualdade (==).
        Compara se duas frações são iguais.
        """
        return self.num == outra_fracao.num and self.den == outra_fracao.den
    
    def __lt__(self, outra_fracao):
        """
        Sobrecarga do operador menor que (<).
        Compara se esta fração é menor que outra.
        """
        return self.num * outra_fracao.den < outra_fracao.num * self.den

    def __gt__(self, outra_fracao):
        """
        Sobrecarga do operador maior que (>).
        Compara se esta fração é maior que outra.
        """
        return self.num * outra_fracao.den > outra_fracao.num * self.den
    
    def __le__(self, outra_fracao):
        """
        Sobrecarga do operador menor ou igual (<=).
        Compara se esta fração é menor ou igual a outra.
        """
        return self.num * outra_fracao.den <= outra_fracao.num * self.den
    
    def __ge__(self, outra_fracao):
        """
        Sobrecarga do operador maior ou igual (>=).
        Compara se esta fração é maior ou igual a outra.
        """
        return self.num * outra_fracao.den >= outra_fracao.num * self.den
    
    def __ne__(self, outra_fracao):
        """
        Sobrecarga do operador diferente (!=).
        Compara se duas frações são diferentes.
        """
        return not self == outra_fracao
    
# --- Bloco de Teste ---
# Este código só executa se você rodar este arquivo diretamente
if __name__ == "__main__":
    
    print("--- Testando a Classe Fração ---")

    # --- 1. Testes de Criação e Simplificação ---
    print("\n--- Testes de Criação e Simplificação ---")
    
    # Frações principais para teste
    f_1_2 = Fracao(1, 2)
    f_1_4 = Fracao(1, 4)
    
    print(f"Fração 1/2: {f_1_2}")
    print(f"Fração 1/4: {f_1_4}")

    # Teste de simplificação automática
    f_5_10 = Fracao(5, 10)
    print(f"Teste de simplificação (5/10): {f_5_10}") # Esperado: 1/2

    # Teste de simplificação para inteiro
    f_8_4 = Fracao(8, 4)
    print(f"Teste de inteiro (8/4): {f_8_4}") # Esperado: 2

    # Teste de padronização de sinal
    f_sinal = Fracao(1, -2)
    print(f"Teste de sinal (1/-2): {f_sinal}") # Esperado: -1/2

    # --- 2. Testes de Operações Aritméticas ---
    print("\n--- Testes de Operações Aritméticas ---")
    
    # Teste de soma (+)
    f_soma = f_1_2 + f_1_4
    print(f"Soma ({f_1_2} + {f_1_4}): {f_soma}") # Esperado: 3/4
    
    # Teste de subtração (-)
    f_sub = f_1_2 - f_1_4
    print(f"Subtração ({f_1_2} - {f_1_4}): {f_sub}") # Esperado: 1/4

    # Teste de multiplicação (*)
    f_mul = f_soma * f_1_4  # Usando o resultado da soma (3/4)
    print(f"Multiplicação ({f_soma} * {f_1_4}): {f_mul}") # Esperado: 3/16

    # Teste de divisão (/)
    f_div = f_soma / f_1_4  # (3/4) / (1/4)
    print(f"Divisão ({f_soma} / {f_1_4}): {f_div}") # Esperado: 3
    
    # Teste iadd (+=)
    print(f"Valor de f_1_2 antes do +=: {f_1_2}")
    f_1_2 += f_1_4 # f_1_2 (1/2) + f_1_4 (1/4) = 3/4
    print(f"Valor de f_1_2 após += {f_1_4}: {f_1_2}") # Esperado: 3/4
    
    # --- 3. Testes de Operações de Comparação ---
    print("\n--- Testes de Operações de Comparação ---")
    # Reutilizando frações: f_1_2 (agora 3/4), f_1_4 (1/4), f_5_10 (1/2)
    
    # Vamos redefinir f_1_2 para 1/2 para facilitar os testes
    f_1_2 = Fracao(1, 2) 

    # Teste de igualdade (==)
    print(f"Teste de Igualdade ({f_1_2} == {f_5_10}): {f_1_2 == f_5_10}") # Esperado: True

    # Teste de diferença (!=)
    print(f"Teste de Diferença ({f_1_2} != {f_1_4}): {f_1_2 != f_1_4}") # Esperado: True
    print(f"Teste de Diferença ({f_1_2} != {f_5_10}): {f_1_2 != f_5_10}") # Esperado: False

    # Teste de menor que (<)
    print(f"Teste Menor Que ({f_1_4} < {f_1_2}): {f_1_4 < f_1_2}") # Esperado: True
    print(f"Teste Menor Que ({f_1_2} < {f_1_4}): {f_1_2 < f_1_4}") # Esperado: False

    # Teste de maior que (>)
    print(f"Teste Maior Que ({f_1_2} > {f_1_4}): {f_1_2 > f_1_4}") # Esperado: True

    # Teste de menor ou igual a (<=)
    print(f"Teste Menor/Igual ({f_1_4} <= {f_1_2}): {f_1_4 <= f_1_2}") # Esperado: True (caso menor)
    print(f"Teste Menor/Igual ({f_1_2} <= {f_5_10}): {f_1_2 <= f_5_10}") # Esperado: True (caso igual)

    # Teste de maior ou igual a (>=)
    print(f"Teste Maior/Igual ({f_1_2} >= {f_1_4}): {f_1_2 >= f_1_4}") # Esperado: True (caso maior)
    print(f"Teste Maior/Igual ({f_1_2} >= {f_5_10}): {f_1_2 >= f_5_10}") # Esperado: True (caso igual)

    print("\n--- Testes Concluídos ---")
