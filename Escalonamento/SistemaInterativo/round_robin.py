from process_getters import get_process_list
import time

quantum = 20

def round_robin(process_dict):
  if len(process_dict) == 0:
    return

  total_time = 0
  for i in process_dict:
    total_time += int(process_dict[i][1])


  while(total_time >= 0):
    to_del = []
    for i in process_dict:
      process_info = process_dict[i]
      process_service_time = int(process_info[1])

      print(f'''
      \r\tExecutando {i}:
        \r\ttempo de execução: {process_service_time}
        \r\ttempo de quantum: {quantum}
        \r\tcomando de invocação: {process_info[3]}
        \r\tusuario: {process_info[-1]}
      ''')

      time.sleep(quantum/10)

      total_time-=quantum
      process_service_time-=quantum

      if process_service_time <= 0:
        to_del.append(i)

      process_info[1] = process_service_time

    for key in to_del:
      del process_dict[key]

process_dict:dict = get_process_list('casos_teste/arq_sis_interativo.csv')
round_robin(process_dict)
print("Todos os processos foram finalizados")
