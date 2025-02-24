import numpy as np
def X(v,w):
  if (((2*v*w/10) % (2* np.pi)) >  np.pi / 2) and (((2*v*w/10) % (2* np.pi)) <  3* np.pi / 2):
    print('It is Tail')
  else:
    print('It is head')
v,w = (2.4,200*2*np.pi)
X(v,w) ## It is head
