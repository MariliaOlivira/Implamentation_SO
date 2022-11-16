from batch_generator import obj_generate_ordered
import time

process_list = dict(obj_generate_ordered('casos_teste/arq.csv'))

for i in process_list:
  process_info = process_list[i]
  process_service_time = int(process_info[1])

  print(f'''
  Executando {i}:
    tempo de execução: {process_service_time}
    comando de invocação: {process_info[3]}
    usuario: {process_info[-1]}
  ''')

  time.sleep(process_service_time/10)

print("Todos os processos foram finalizados")
