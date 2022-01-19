import math
import numpy as np
import requests

def cosangle_lines(line1,line2): # https://stackoverflow.com/a/23989588/5566957
  dx1 = line1[1][0] - line1[0][0]
  dy1 = line1[1][1] - line1[0][1]
  dx2 = line2[1][0] - line2[0][0]
  dy2 = line2[1][1] - line2[0][1]
  cosangle = abs((dx1*dx2 + dy1*dy2) / math.sqrt((dx1**2 + dy1**2) * (dx2**2 + dy2**2)))
  return cosangle

def getFML(id,apikey):
  url = "https://floorplanner.com/api/v2/projects/"+id+".fml"
  headers = {
    "Accept": "application/fml",
    "Authorization": "Basic "+apikey
  }
  response = requests.request("GET", url, headers=headers)
  return response.text

# znajdywanie przecięcia linii, także na ich przedłużeniu: https://stackoverflow.com/a/20679579/5566957

def fline(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
      
# definicja najbliższego punktu
def closest_node(node, nodes):
    from scipy.spatial import distance # this probably shouldn't be here , but doesn't work if called outside def (?)
    distances = distance.cdist([node], nodes)
    closest_index = distances.argmin()
    dist = distances.min()
    return closest_index, dist
