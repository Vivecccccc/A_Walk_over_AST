import copy

def parsing(ast, is_init=True):
  global stalker, res, ind
  if is_init:
    stalker = 0
    res = []
    is_init = False
    ind = []
  stack = []
  if isinstance(ast, list):
    for i, elem in enumerate(ast):
      ind.append(i)
      stack.append(stalker)
      parsing(elem, is_init)
      stalker += 1
      stack.append(stalker)
      res.append(copy.deepcopy([stack, ind]))
      stack = []
      ind.pop()
  else:
    pass
  return res
