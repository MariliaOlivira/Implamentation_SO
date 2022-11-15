from multipledispatch import dispatch

class Priority():
  @dispatch(int, float)
  def __init__(self, priority_level, quantum):
    self.priority_level = priority_level
    self.quantum = quantum

  @dispatch(int)
  def __init__(self, priority_level):
    self.priority_level = priority_level

class Process():
  @dispatch(str, int, float, float)
  def __init__(self, name, priority, service_time, quantum):
    self.name = name
    self.service_time = service_time
    self.priority = Priority(priority, quantum)

  @dispatch(str, float, float)
  def __init__(self, name, service_time, quantum) -> None:
    self.name = name
    self.service_time = service_time
    self.quantum = quantum

  @dispatch(str, int, float)
  def __init__(self, name, priority, service_time) -> None:
    self.name = name
    self.service_time = service_time
    self.priority = Priority(priority)

  @dispatch(str, int)
  def __init__(self, name, service_time):
    self.name = name
    self.service_time = service_time
