from process_getters import get_process_list, new_process_bach
import time

quantum = 20

def round_robin(process_dict, to_add = False, round = 1):
  if len(process_dict) == 0:
    return

  if not to_add:
    to_add = True

  to_del = []
  print(f"Executando a rodada {round}")

  for i in process_dict:
    process_info = process_dict[i]
    process_service_time = int(process_info[1])

    print(f'''
    \rExecutando {i}:
      \r\ttempo de execução: {process_service_time}
      \r\ttempo de quantum: {quantum}
      \r\tcomando de invocação: {process_info[3]}
      \r\tusuario: {process_info[-1]}
    ''')

    time.sleep(quantum/10)

    process_service_time-=quantum

    if process_service_time <= 0:
      to_del.append(i)

    process_info[1] = process_service_time

  if to_add and round == 1:
    print("Recebendo novos processos\n")
    new_process_bach('casos_teste/arq_sis_interativo2.csv', process_dict)

  for key in to_del:
    del process_dict[key]

  round += 1
  round_robin(process_dict, True, round)
  return

process_dict:dict = get_process_list('casos_teste/arq_sis_interativo.csv')
round_robin(process_dict)
print("Todos os processos foram finalizados")
