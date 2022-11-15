import csv, time

def obj_generate_ordered(file_client):
  obj = []
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    enumerate_tuple_result = enumerate(arq)

    for i in enumerate_tuple_result:
      obj.append(i)

  return sorted(obj, key= lambda x: int(x[1][1]))

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
