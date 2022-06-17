import unittest
import population
import simulation 
import genome 
import creature 
import numpy as np

class TestGA(unittest.TestCase):
    def testBasicGA(self):
        pop = population.Population(pop_size=10, 
                                    gene_count=3)
        #sim = simulation.ThreadedSim(pool_size=1)
        sim = simulation.Simulation()

        for iteration in range(1000):
            # this is a non-threaded version 
            # where we just call run_creature instead
            # of eval_population
            for cr in pop.creatures:
                sim.run_creature(cr, 2400)            
            #sim.eval_population(pop, 2400)
            fits = [cr.get_distance_travelled() 
                    for cr in pop.creatures]
            links = [len(cr.get_expanded_links()) 
                    for cr in pop.creatures]
            print(iteration, "fittest:", np.round(np.max(fits), 3), 
                  "mean:", np.round(np.mean(fits), 3), "mean links", np.round(np.mean(links)), "max links", np.round(np.max(links)))       
            fit_map = population.Population.get_fitness_map(fits)
            new_creatures = []
            for i in range(len(pop.creatures)):
                p1_ind = population.Population.select_parent(fit_map)
                p2_ind = population.Population.select_parent(fit_map)
                p1 = pop.creatures[p1_ind]
                p2 = pop.creatures[p2_ind]
                # now we have the parents!
                dna = genome.Genome.crossover(p1.dna, p2.dna)
                dna = genome.Genome.point_mutate(dna, rate=0.1, amount=0.25)
                dna = genome.Genome.shrink_mutate(dna, rate=0.25)
                dna = genome.Genome.grow_mutate(dna, rate=0.1)
                cr = creature.Creature(1)
                cr.update_dna(dna)
                new_creatures.append(cr)
            # elitism
            max_fit = np.max(fits)
            for cr in pop.creatures:
                if cr.get_distance_travelled() == max_fit:
                    new_cr = creature.Creature(1)
                    new_cr.update_dna(cr.dna)
                    new_creatures[0] = new_cr
                    filename = "elite_"+str(iteration)+".csv"
                    genome.Genome.to_csv(cr.dna, filename)
                    break
            
            pop.creatures = new_creatures
                            
        self.assertNotEqual(fits[0], 0)


        # pop = poplib.Population(pop_size=20, gene_count=4)
        # sim = simlib.Simulation()
        # sim = simlib.ThreadedSim(pool_size=8)
        # sim.eval_population(pop, 2400)
        # for generation in range(20):
        #     for cr in pop.creatures:
        #         sim.run_creature(cr, 2400)
        #     fits = [cr.get_distance_travelled() for cr in pop.creatures]
        #     fitmap = poplib.Population.get_fitness_map(fits)

            # print(generation, np.max(fits), np.mean(fits))

            # fmax = np.max(fits)
            # for cr in pop.creatures:
            #     if cr.get_distance_travelled() == fmax:
            #         elite = cr
            #         break

            # new_gen = []
            # for cid in range(len(pop.creatures)):
            #     p1_ind = poplib.Population.select_parent(fitmap)
            #     p2_ind = poplib.Population.select_parent(fitmap)
            #     dna = genlib.Genome.crossover(pop.creatures[p1_ind].dna, pop.creatures[p2_ind].dna)
            #     dna = genlib.Genome.point_mutate(dna, 0.1, 0.25)
            #     dna = genlib.Genome.grow_mutate(dna, 0.25)
            #     dna = genlib.Genome.shrink_mutate(dna, 0.25)
            #     cr = crlib.Creature(1)
            #     cr.set_dna(dna)
            #     new_gen.append(cr)

            # new_gen[0] = elite
            # csv_filename = str(generation) + '_elite.csv'
            # genlib.Genome.to_csv(elite.dna, csv_filename)
            # pop.creatures = new_gen

unittest.main()
