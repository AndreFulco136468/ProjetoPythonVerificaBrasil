from cep_br import CepBr
import re


cep = 78056071

cep_objeto = CepBr(cep)
bairro, localidade = cep_objeto.Acesso_cep()
print(bairro, localidade)

