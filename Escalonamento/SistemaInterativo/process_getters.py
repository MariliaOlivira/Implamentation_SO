import csv

FILE_TEST_PATH_1 = 'casos_teste/arq_sis_interativo.csv'
FILE_TEST_PATH_2 = 'casos_teste/arq_sis_interativo2.csv'

def get_process_list(file_client) -> dict:
  obj = dict()
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    for i in enumerate(arq):
      obj[i[1][0]] = i[1]

  return obj

def new_process_bach(file_client, current_bach):
  new_batch = get_process_list(file_client)

  for i in new_batch:
    current_bach[i] = new_batch[i]

def priority_queue_generator(file_client) -> dict:
  obj = [[] for i in range(5)]

  add_process_by_priority(file_client, obj)

  return obj

def add_process_by_priority(file_client, current_bach):
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    for i in enumerate(arq):
      info = i[1]
      priority = 5 - int(info[2])
      current_bach[priority].append(info)

def new_process_bach(file_client, current_bach):
  new_batch = get_process_list(file_client)

  for i in new_batch:
    current_bach[i] = new_batch[i]


def job_log(process_info ,quantum = 0):
  process_service_time = int(process_info[1])

  if quantum:
    print(f'''
    \rExecutando {process_info[0]}:
      \r\ttempo de execução: {process_service_time}
      \r\ttempo de quantum: {quantum}
      \r\tcomando de invocação: {process_info[3]}
      \r\tusuario: {process_info[-1]}
    ''')
  else:
    print(f'''
    \rExecutando {process_info[0]}:
      \r\ttempo de execução: {process_service_time}
      \r\tcomando de invocação: {process_info[3]}
      \r\tusuario: {process_info[-1]}
    ''')
