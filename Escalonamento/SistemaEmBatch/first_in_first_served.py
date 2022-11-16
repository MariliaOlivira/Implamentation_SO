from copy import deepcopy
from batch_generator import *
import time

def fifs_escalonator(process_batch:dict):
  try:
    i = list(process_batch.keys())[0]
  except IndexError:
    return

  process_info = process_batch[i]
  process_service_time = int(process_info[1])

  if i[1] == '3':
    print("Recebendo novo lote de processos")
    new_process_bach(file_path2, process_batch)

  print(f'''
  Executando {i}:
    tempo de execução: {process_service_time}
    comando de invocação: {process_info[3]}
    usuario: {process_info[-1]}
  ''')

  time.sleep(process_service_time/10)

  if len(process_batch) == 0:
    return

  del process_batch[i]

  fifs_escalonator(process_batch)
  return


file_path1 = 'casos_teste/arq.csv'
file_path2 = 'casos_teste/arq2.csv'

process_batch = obj_generate(file_path1)

fifs_escalonator(process_batch)

print("Todos os processos foram finalizados")
