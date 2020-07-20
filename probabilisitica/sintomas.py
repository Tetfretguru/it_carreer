"""Con recursividad y cantidad de test elegidos por el user """

def calc_bayes(prior_A, prob_B_dado_A, prob_B):
	return (prior_A * prob_B_dado_A) / prob_B

def main(i):
	
	prob_cancer = i / 100000
	prob_sintoma_dado_cancer = 1
	prob_sintoma_dado_no_cancer = 10 / 99999
	prob_no_cancer = 1 - prob_cancer

	prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer) 

	prob_cancer_dado_sintoma =  calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

	return prob_cancer_dado_sintoma

if __name__ == '__main__':
	tests = int(input('Cuantos tests quiere hacer?: '))
	resultados = []
	i = 1.0
	
	for _ in range(tests):
		nuevo_prior = main(i)
		i = nuevo_prior
		nu = main(nuevo_prior)
		resultados.append(nuevo_prior)

	indice = 1
	for result in resultados:
		print(f'Intento {indice}, probabilidad: {result}')
		indice += 1

		
	

	