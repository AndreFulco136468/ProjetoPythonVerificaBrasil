from validate_docbr import CPF, CNPJ



class Documento:
    
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento invalido')
        
        
class DocCpf:
    
    def __init__(self, documento):
        self.cpf = documento
        self.valida()
        
        
    def __str__(self):
        
        # cpf = CPF()
        # return cpf.mask(self.cpf)
        return self.formatado()
       
    
    
    def valida(self):
        validador = CPF()
        if validador.validate(self.cpf):
            return True
        else:
            raise ValueError('Cpf invalido')
        
        
    def formatado(self):
        
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    
    
class DocCnpj:
    
    def __init__(self, documento):
        self.cnpj = documento
        self.validador()
        
        
    def __str__(self):
        # mascara = CNPJ()
        # return mascara.mask(self.cnpj)
        return self.formatado()
    
    def validador(self):
        cnpj_valido = CNPJ()
        if cnpj_valido.validate(self.cnpj):
            return True
        else:
            raise ValueError('Cnpj invalido')
        
    def formatado(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
        
    
    
        
        
        
        
        
#######################################################






# class CpfCnpj:
    
#     def __init__(self, documento, tipo):
#         documento_entrada = str(documento)
#         self.tipo = str(tipo).lower()
#         documento = str(documento_entrada)
#         if self.tipo == 'cpf':
#             if self.valida_cpf(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError('CPF inválido')    
#         elif self.tipo == 'cnpj':
#             if self.valida_cnpj(documento):
#                 self.cnpj = documento                
#             else:
#                 raise ('CNPJ inválido')
        
        
        
        
#     def valida_cpf(self,cpf):
#         if len(cpf) == 11:
#             cpf_valido = CPF()
#             return cpf_valido.validate(cpf)
#         else:
#             raise ValueError("Erro na quantidade de numeros")
    
#     def valida_cnpj (self,cnpj):
#         if len(cnpj) == 14:
#             cnpj_valido = CNPJ()
#             return cnpj_valido.validate(cnpj)
#         else:
#             raise ValueError('Quantidade de numeros invalida')
                
        
#     def format_cpf(self, cpf):
#         cpf_formatado = CPF()
#         return cpf_formatado.mask(cpf)
    
#     def format_cnpj(self, cnpj):
#         cnpj_formatado = CNPJ()
#         return cnpj_formatado.mask(cnpj)
    
#     def __str__(self):
#         if self.tipo == 'cpf':
#             return self.format_cpf(self.cpf)
#         elif self.tipo == 'cnpj':
#             return self.format_cnpj(self.cnpj)