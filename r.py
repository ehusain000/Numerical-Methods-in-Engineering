import numpy as np



A = np.array([[0.78, 0.563],
              [0.913, 0.659]])

b = np.array([0.271, 0.254])

x = np.array([0.999, -1.0])



r = b - A@x

print(r)