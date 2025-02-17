from math import tanh
import random
POPULATION_SIZE=4
MUTATION_PROBABILITY=0.1

def func(x):
    return x**2

# generation
population = [random.randint(0,31) for _ in range(POPULATION_SIZE)]

for i in range(10):
    population.sort(key=func, reverse=True)
    print(population)

    selection = population[:2]
    print(selection)

    #crossing
    element_1, element_2 = tuple(population[:2])

    element_1 = format(element_1, '05b')
    print(element_1)
    element_2 = format(element_2, '05b')
    print(element_2)

    new_element_1 = element_1[0:3] + element_2[3:]
    new_element_2 = element_2[0:3] + element_1[3:]
    print(new_element_1, new_element_2)

    new_elements = [new_element_1, new_element_2]

    # mutation
    new_gen = []
    for new_element in new_elements:
        element_list = list(new_element)
        if random.random() < MUTATION_PROBABILITY:
            bit = random.randint(0, 4)
            print(element_list)
            element_list[bit] = '1' if element_list[bit] == 0 else '0'
            print(element_list)
        new_element = int(''.join(element_list), 2) # 2 so it is binary
        print(new_element)
        new_gen.append(new_element)
       

    population += new_gen
    print(sorted(population, key=func, reverse=True))

print(len(population))
print(max(population)) 