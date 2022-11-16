from process_getters import get_process_list, job_log, new_process_bach, FILE_TEST_PATH_1, FILE_TEST_PATH_2
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

    job_log(i, process_info)

    time.sleep(quantum/10)

    process_service_time-=quantum

    if process_service_time <= 0:
      to_del.append(i)

    process_info[1] = process_service_time

  if to_add and round == 1:
    print("Recebendo novos processos\n")
    new_process_bach(FILE_TEST_PATH_2, process_dict)

  for key in to_del:
    del process_dict[key]

  round += 1
  round_robin(process_dict, True, round)
  return

process_dict:dict = get_process_list(FILE_TEST_PATH_1)
round_robin(process_dict)
print("Todos os processos foram finalizados")
