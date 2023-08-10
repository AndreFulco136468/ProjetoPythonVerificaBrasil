from validate_docbr import CPF, CNPJ



class CpfCnpj:
    
    def __init__(self, documento, tipo):
        documento_entrada = str(documento)
        self.tipo = str(tipo).lower()
        documento = str(documento_entrada)
        if self.tipo == 'cpf':
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido')    
        elif self.tipo == 'cnpj':
            if self.valida_cnpj(documento):
                self.cnpj = documento                
            else:
                raise ('CNPJ inválido')
        
        
        
        
    def valida_cpf(self,cpf):
        if len(cpf) == 11:
            cpf_valido = CPF()
            return cpf_valido.validate(cpf)
        else:
            raise ValueError("Erro na quantidade de numeros")
    
    def valida_cnpj (self,cnpj):
        if len(cnpj) == 14:
            cnpj_valido = CNPJ()
            return cnpj_valido.validate(cnpj)
        else:
            raise ValueError('Quantidade de numeros invalida')
                
        
    def format_cpf(self, cpf):
        cpf_formatado = CPF()
        return cpf_formatado.mask(cpf)
    
    def format_cnpj(self, cnpj):
        cnpj_formatado = CNPJ()
        return cnpj_formatado.mask(cnpj)
    
    def __str__(self):
        if self.tipo == 'cpf':
            return self.format_cpf(self.cpf)
        elif self.tipo == 'cnpj':
            return self.format_cnpj(self.cnpj)