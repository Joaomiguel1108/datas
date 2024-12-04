from datetime import datetime, timedelta


data_hora_atual = datetime.now()


nova_data = data_hora_atual + timedelta(days=5)

print("Data e hora após 5 dias:", nova_data.strftime("%D"))
