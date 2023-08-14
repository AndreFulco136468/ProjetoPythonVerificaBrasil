import re

# padrao = "[1-9][a-z]{2}[1-9]"
# texto = "aa1 er4 f3r tyy 1hg9"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao = "\w{5,50}@[a-z]{3,10}.com"
# texto = "andre124678@hotmail.com 51651651651"
# resposta = re.search(padrao, texto)
# print(resposta.group())

class TelBr:
    
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Telefone invalido')
        
    def __str__ (self):
        return self.format_telefone()
        
    
    def valida_telefone(self, telefone):
        texto = telefone
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        phone_valido = re.findall(padrao, texto)
        if phone_valido:
            return True
        else:
            return False
        
    def format_telefone(self):
        padrao  = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        telefone = self.telefone
        telefone_formatado = re.search(padrao, telefone)
        return  f'+{telefone_formatado.group(1)} ({telefone_formatado.group(2)}) {telefone_formatado.group(3)} - {telefone_formatado.group(4)} '
        
        

