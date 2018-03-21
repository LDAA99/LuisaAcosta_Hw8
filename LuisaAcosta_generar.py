import numpy as np

#punto a, al poner de size N ya aseguro la cantidad de datos que me retorna 

def sample_1(N):
	f=np.random.choice(a=[-10, -5, 3, 9], size=N, p=[0.1, 0.4, 0.2, 0.3])
	return f


#punto b

def sample_2(N):
	f=np.random.exponential(scale=0.5, size=N)
	return f
#punto c

def get_mean(sampling_fun, N, M):
	
	for i in range(M):
		v=sampling_fun(N)
		mean=np.mean(v)
		return mean

print get_mean(sample_1, 10, 5)
#punto d



