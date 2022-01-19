import math

def debug(variable):
  print(variable, '=', repr(eval(variable)))

def debugl(variables):
  s=""
  for variable in variables:
    s+=variable+' = '+repr(eval(variable))+'  '
  print(s)

def cosangle_lines(line1,line2): # https://stackoverflow.com/a/23989588/5566957
  dx1 = line1[1][0] - line1[0][0]
  dy1 = line1[1][1] - line1[0][1]
  dx2 = line2[1][0] - line2[0][0]
  dy2 = line2[1][1] - line2[0][1]
  cosangle = abs((dx1*dx2 + dy1*dy2) / math.sqrt((dx1**2 + dy1**2) * (dx2**2 + dy2**2)))
  return cosangle
