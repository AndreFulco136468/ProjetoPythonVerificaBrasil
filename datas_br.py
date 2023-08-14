from datetime import datetime, timedelta

class DataCadastro:
    
    def __init__(self):
        self.data_cadastro = datetime.now()
        
        
        
    def __str__(self):
        return self.data_formatada()
    
    
    def mes_do_ano(self):
        mes_do_ano=[
            "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "Agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cad = self.data_cadastro
        return mes_do_ano[mes_cad.month - 1]
    
    def dia_da_semana(self):
        dias_da_semana=[
            "segunda",  "Terça", "quarta", "Quinta", "Sexta", "Sabado", "Domingo"
        ]
        dia_semana = self.data_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def data_formatada (self):
        format_data = self.data_cadastro.strftime("%d/%m/%y %H:%M")
        return format_data
    
    def tempo_de_cadastro (self):
        hoje = (datetime.today() + timedelta(days=30, hours=59)) - self.data_cadastro
        return hoje
    