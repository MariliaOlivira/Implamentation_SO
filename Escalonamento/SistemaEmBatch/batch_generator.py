import csv

def obj_generate(file_client) -> dict:
  obj = dict()
  with open(file_client, 'r') as file:
    arq = csv.reader(file, delimiter=";")
    for i in enumerate(arq):
      obj[i[1][0]] = i[1]

  return obj

def new_process_bach(file_client, current_bach):
  new_batch = obj_generate(file_client)

  for i in new_batch:
    current_bach[i] = new_batch[i]