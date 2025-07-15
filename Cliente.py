class Cliente:
    def __init__(self, n, fone):
    # 1 Underline antes  = Protected
    # 1 Underline depois = Public
    # 2 Underline antes  = Private
        self._nome = n
        self._telefone = fone

    # Método GET (Get é usado para
    # ler o valor de um atributo de um objeto)
    def get_nome(self):
        return self._nome

    # Método Set recebe um valor para ser
    # Guardado em um atributo
    def set_nome(self, nome):
        self._nome = nome



