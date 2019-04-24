import numpy
import matplotlib.pyplot as plt
import math
import random
from functools import reduce

prior_dist= [0.1, 0.2, 0.4, 0.2, 0.1]
hyps = [1, .75, .5, .25, 0] # probabilty for cherry p. so for lime it would be 1-p
posteriorsData = [[], [], [], [], []]
data =[]

def generate_data(h, n):
    '''
    Function to generate samples of data.
    :param h: which hypothesis to use
    :param n: number of samples
    :return: sample data
    '''

    hyp = hyps[h]


    for i in range(0,n):
        d= 1 if random.uniform(0, 1) <= hyp else 0
        data.append(d)

    return data

def compute_probabilities(n):
    '''
    Computing probabilities that each hypothesis is true given n data points.
    :param n: data points
    :return:
    '''

    posteriors = []


    for i in range(0,len(hyps)):
        hyp = hyps[i]
        prior = prior_dist[i]
        probability_of_hyp = prior #initially prob is the prior

        for j in range(0,n):
            d= data[j]
            likelihood = hyp if d==1 else 1-hyp
            probability_of_hyp = probability_of_hyp*likelihood
        posteriors.append(probability_of_hyp)

    # sum= posteriors.reduce((a, b) => a + b, 0)
    sum1= reduce((lambda x, y: x + y), posteriors)
    # posteriors = posteriors.map(posterior= > posterior / sum)

    posteriors = list(map((lambda p:p/sum1), posteriors))

    for i in range(0,len(posteriors)):
        posteriorsData[i].append(posteriors[i])
        prior_dist[i] = posteriors[i]

def generate_graph():

    for n in range(0,10):
        compute_probabilities(n)

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.plot(labels, posteriorsData[0], 'b-', label='h1')
    plt.plot(labels, posteriorsData[1], 'g-', label='h2')
    plt.plot(labels, posteriorsData[2], 'r-', label='h3')
    plt.plot(labels, posteriorsData[3], 'p-', label='h4')
    plt.plot(labels, posteriorsData[4], 'y-', label='h5')
    plt.legend(loc='best')
    plt.show()






if __name__ == '__main__':
    generate_data(2, 10)
    generate_graph()