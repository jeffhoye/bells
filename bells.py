'''
Created on May 9, 2016

@author: jeffh
'''
import numpy as np
import math

DIM = 5 # dimension

correlation = {} # angle to [sum, samples] -- average is sum/samples

def gen_rand_vecs(number):
  vecs = np.random.normal(size=(number,DIM))
  mags = np.linalg.norm(vecs, axis=-1)
  return vecs / mags[..., np.newaxis]
  
def addSamples(angle, number):
#   m1 = np.array([1.,0.,0.])
  m1_b = [1.,]
  for x in range(DIM-1):
    m1_b.append(0.)
  m1 = np.array(m1_b)
  
#   m2 = np.array([math.cos(angle),math.sin(angle),0.])
  m2_b = [math.cos(angle),math.sin(angle)]
  for x in range(DIM-2):
    m2_b.append(0.)
  m2 = np.array(m2_b)
  
#   print m1, m2

  global correlation
  if angle not in correlation:
    correlation[angle] = [0,0]
  sum = correlation[angle][0]
  samples = correlation[angle][1]
  
  singlets = gen_rand_vecs(number)
  for s in singlets:
    correlate = -1
    if m1.dot(s) > 0:
      if m2.dot(s) > 0:
        correlate = 1
    else:
      if m2.dot(s) < 0:
        correlate = 1
#     print correlation
    sum+=correlate
  samples+=number
  correlation[angle] = [sum,samples]
  return 1.0*sum/samples
  
  
def main():
  numRange = 16
  for p in range(numRange):
    angle = 2.0*p*math.pi/numRange    
    c = addSamples(angle,100000)
    print "%f,%f" % (angle, c)
    
if __name__ == "__main__":
#   singlet = randVec()
  main()