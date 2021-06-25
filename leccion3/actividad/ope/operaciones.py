class operacionesMatematicas:
    """
    Operaciones matematicas
    Atributos
    ---------
    op1:
        este es el primer operando (int o float) que se utilizara en las operaciones
    op2:
        este es el segundo operando (int o float) que se utilizara en las operaciones

    Metodos
    -------

    suma:
        Suma los operandos op1 y op2
    resta:
        Resta los operandos op1 y op2
    producto:
        Multiplica los operandos op1 y op2
    division:
        Divide los operandos op1 y op2
    primo:
        Determina si el operando op1 es primo

    Ejemplos
    --------
    >>> import operacionesMatematicas
    >>> oM = operacionesMatematicas(5, 8)
    >>> res_suma = oM.suma()
    >>> res_producto = oM.producto()
    """

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def suma(self):
        """
        Metodo suma. Aplica el algoritmo de la suma sobre los operandos op1 y op2
        Inputs:
        -------
            self.op1
            self.op2
        Outputs:
        --------
            res: resultado de sumar op1 y op2
        """
        res = self.op1 + self.op2
        return res

    def resta(self):
        """
        Metodo resta. Aplica el algoritmo de la resta sobre los operandos op1 y op2
        Inputs:
        -------
            self.op1
            self.op2
        Outputs:
        --------
            res: resultado de restar op1 y op2
        """
        res = self.op1 - self.op2
        return res

    def producto(self):
        """
        Metodo producto. Aplica el algoritmo de la multiplicacion sobre los operandos op1 y op2
        Inputs:
        -------
            self.op1
            self.op2
        Outputs:
        --------
            res: resultado de multiplicar op1 por op2
        """
        res = self.op1 * self.op2
        return res

    def division(self):
        """
        Metodo division. Aplica el algoritmo de la division sobre los operandos op1 y op2
        Si op2 (denominador) es igual a 0, devolvera 0
        Inputs:
        -------
            self.op1
            self.op2
        Outputs:
        --------
            res: resultado de dividir op1 entre op2
        """
        res = self.op1 / self.op2 if(self.op2 != 0) else 0
        return res

    def primo(self):
        """
        Metodo primo. Determina si op1 es primo
        Inputs:
        -------
            self.op1
        Outputs:
        --------
            True si op1 es primo, False si es lo contrario
        """
        es_primo = True
        for i in(2, self.op1 - 1):
            if(self.op1 % i == 0):
                es_primo = False
        return es_primo
