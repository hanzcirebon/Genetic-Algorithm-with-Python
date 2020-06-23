import random
import numpy

#initialize Maximum Population, can be change
max_pop = 100

#initialize Generation
numof_generation = 50

#max chromosome size, can be change
max_gens = 6

def main():
    
    global max_pop
    global numof_generation
    global max_gens

    #creating phenotype population
    phenotype_population = []

    #initial population / chromosome array
    initial_population = create_genotype_population(max_pop)

    for i in range(numof_generation):

        print("=========================",i+1,"-Generation===========================")

        #gens array that has the seperated x and y
        gensxy = split_xy(initial_population)

        phenotype_population = decode(gensxy[0],gensxy[1])
        print("")
        
        initial_population = generation(initial_population,phenotype_population)
        
        
#creating genotype population
def create_genotype_population (max_pop):

    initial_population = []
    max_pop
    max_gens
    
    for i in range (max_pop):
        
        gens = []

        #creating gen
        for i in range(max_gens):

            num = numpy.random.uniform(low=0,high=1)
            
            gens.append(num)

        #insert chromosome value
        initial_population.append(gens)

    return initial_population

#decoding
def decode(gensx,gensy):
    
    max_gens

    totx_arr = []
    toty_arr = []
    for i in range(len(gensx)):
        totx = 0
        toty = 0
        for j in range(len(gensx[0])):
            totx += (gensx[i][j])
            toty += (gensy[i][j])

        totx_arr.append(totx)
        toty_arr.append(toty)
        
    
    tot = int(max_gens/2)
    phenotype_population = []
    sum = 0
    for i in range(len(gensx)):

        arrayx = (-3) + ((3 + (3))/tot) * (totx_arr[i])
        arrayy = (-2) + ((2 + (2))/tot) * (toty_arr[i])
            
        phenotype_population.append([arrayx,arrayy])

    return phenotype_population
    
#split initial population into x population and y population
def split_xy (initial_population):

    max_gens
    
    suma = 0
    
    div = int(max_gens / 2)
    
    gensx = []
    gensy = []
    
    for i in range(len(initial_population)):
        
        arrayx = []
        arrayy = []
        sum = 0
        
        for j in range(div):
            arrayx.append(initial_population[suma][sum])
            sum+=1
            
        for j in range(div,max_gens):
            arrayy.append(initial_population[suma][sum])
            sum+=1

        gensx.append(arrayx)
        gensy.append(arrayy)

        suma+=1

    gensxy = [gensx,gensy]

    return gensxy

#looping the main program will return new generation
def generation (initial_population, phenotype_population):

    fitness = []
    sum = 0

    for i in range(len(phenotype_population)):

        fitness.append(Fitness(phenotype_population[sum][0],phenotype_population[sum][1]))
        sum+=1

    Tournament_Result = selection(fitness, phenotype_population)

    #create new parent
    new_parent = []
    sum = 0
    for i in range(len(Tournament_Result)):
        new_parent.append(initial_population[Tournament_Result[sum]])
        sum+=1

    #crossover child and parent to get new generation
    prob_Crossover = 0.5
    random = numpy.random.uniform(low=0,high=1)
    
    #crossover
    crosspoint = numpy.random.randint(0, len(initial_population[0]))

    pop_crossover = new_parent
    sum = crosspoint
    
    for i in range(crosspoint,len(initial_population[0])):
        pop_crossover[0][sum] = new_parent[1][sum]
        pop_crossover[1][sum] = new_parent[0][sum]
        sum+=1

    #initialize mutation probability
    prob_mutation = 0.01

    for i in range(len(new_parent)):
        rand = numpy.random.uniform(low=0,high=1)
        if rand < prob_mutation :
            mrand = numpy.random.randint(0, len(initial_population[0]))
            mutate = numpy.random.uniform(low=0,high=1)
            new_parent[i][mrand] = mutate

    #generate new generation of population
    new_generation = initial_population
    new_gen_fitness = fitness

    for i in range(len(new_parent)):

        num_worst_fitness = new_gen_fitness.index(min(new_gen_fitness))
        new_generation[num_worst_fitness] = new_parent[i]

    idx_best = fitness.index(min(fitness))
    print("best chromosome : ", initial_population[idx_best])
    print("best Fitness    : ", min(fitness))
    print("x1              : ", phenotype_population[idx_best][0])
    print("x2              : ", phenotype_population[idx_best][1])

    return new_generation

#===============Parent Selection=================
#use tournament selection
def selection(fitness, population):

    #calculate the total of Fitness
    div = 0
    divider = 0
    for i in range(len(fitness)):

        divider += fitness[div]
        div += 1
        
    #calculate probability
    prob = []
    sum = 0
    for i in range(len(fitness)):

        count = fitness[sum]/divider
        prob.append(count)
        sum += 1

    tournament_size = 2     #the number of parent that will be selected.
    best = []
    for i in range(tournament_size):
        best.append(tournament_sel(population,fitness))

    return best

#============Tournament Game=============
def tournament_sel(population,fitness):
    best = []
    for i in range(3):
        ind = random.randint(0,len(population)-1)
        if (best == []) or fitness[ind] > fitness[best]:
            best = ind
            
    return best


#==========this function will return the result of the Fitness=========
def Fitness(x,y):
    
    #define the objective function. suppose the x1 is x, and x2 is y
    
    Objective = (4 - 2.1 * x**2 + x**4 / 3) * x**2 + x*y + ((-4) + 4 * y**2) * y**2

    #f = 1/(h+a) to minimize.
    return (1/(Objective + 0.00001))

if __name__ == '__main__':
    main()
