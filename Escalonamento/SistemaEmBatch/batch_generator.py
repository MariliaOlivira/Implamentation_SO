import csv

def obj_generate(file_client) -> dict:
  obj = dict()
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    for i in enumerate(arq):
      obj[i[1][0]] = i[1]

  return obj

def obj_generate_ordered(file_client):
  obj = []
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    enumerate_tuple_result = enumerate(arq)

    for i in enumerate_tuple_result:
      obj.append(i)

  return sorted(obj, key= lambda x: int(x[1][1]))

def new_process_bach(file_client, current_bach):
  new_batch = obj_generate(file_client)

  for i in new_batch:
    current_bach[i] = new_batch[i]
