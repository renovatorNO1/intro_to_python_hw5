# solution functions for percolation assignment part 1

import numpy as np
import matplotlib.pyplot as plt


def read_grid(infile_name):
    '''Creates a 2 dimensional sites[][] array of booleans from a file input'''

    infile = open(infile_name, 'r')

    #read the first line and convert to an integer
    n = int(infile.readline())

    #load the rest of the array
    a = np.fromstring(infile.read(), dtype = int, sep=' ')
    a.shape = (n,n)
    
    infile.close()

    #make the sites array noting that it is the logical negation of a
    sites = a.astype(int)


    return sites


def write_grid(filename, sites):
    '''Writes the sites[][] array to a file in the correct format'''


    #write the array sites to the file
    np.savetxt(filename, sites.astype(int), fmt = "%d", header = str(sites.shape[0]),\
        comments='')



def vertical_flow(sites):
    '''returns an array of full sites due to vertical percolation on the input'''
    #create the array full as a copy of sites
    full=np.array(sites)

    #since the first row has now already been initialized we fill the rest
    for i in range(1,len(sites)):
        for j in range(len(sites)):
            if full[i-1, j] == 1 and sites[i,j] == 1:
                full[i,j] = 1
            else:
                full[i,j] = 0

    return full


def percolates(flow_matrix):
    '''determines if the flow percolates given the array full'''
    #we simply need to check the bottom row of full
    result = bool(sum(flow_matrix[len(flow_matrix)-1]))

    return result


def make_sites(n, p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    #make an array of 1s and zeros using binomial
    sites=np.random.binomial(1,p,(n,n))

    return sites

    
def flow_from(sites, full, i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    if i < 0 or j >= len(full):
        return
    if j < 0 or i >= len(full):
        return
    if sites[i][j] == 0:
        return
    if full[i][j] == 1:
        return

    full[i][j] = True
    flow_from(sites,full,i+1,j)
    flow_from(sites, full, i-1, j)
    flow_from(sites,full,i,j+1)
    flow_from(sites,full,i, j-1)

    
def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """
    # make the array full, all 0 to start
    full=np.zeros(sites.shape)

    #for each site in the top row determine flow
    for j in range(sites.shape[1]):
        flow_from(sites,full,0,j)
    #now return full    
    return full.astype(int)

def show_perc(sites):
    '''displays a visualization of the flow in sites'''
    #make an array of integers 0-blocked, 1-vacant, 2-full
    full = undirected_flow(sites)
    v = sites.astype(int) + full.astype(int)
    plt.matshow(v)
    plt.show()


def make_plot_dynamic(trials, size, tolerance):
    x = np.array([0,1]).astype(float)
    y = np.array([0,1]).astype(float)

    i = 0

    while i < len(x) - 1:
        if abs(y[i + 1] - y[i]) < tolerance:
            i += 1
            continue

        count = 0
        x_new = (x[i] + x[i+1])/2
        for j in range(trials):
            count += percolates(undirected_flow(make_sites(size, x_new)))
        x = np.insert(x, i + 1, x_new)
        y = np.insert(y, i + 1, count/float(trials))

    plt.plot(x, y)
    plt.show()


def make_plot_standard(trials, size):

    x = np.concatenate((np.linspace(0, 0.3, 40), np.linspace(0.3, 0.8, 70), \
                        np.linspace(0.8, 1, 40))).astype(float)
    y = np.zeros(x.shape).astype(float)

    for i in range(len(x)):
        count = 0
        for j in range(trials):
            count += percolates(undirected_flow(make_sites(size, x[i])))
        y[i] = count/trials

    plt.plot(x, y)
    plt.show()


def make_plot(size, trials, tolerance = 0.025):
    
    if trials < 5000:
        make_plot_standard(trials, size)
    else:
        make_plot_dynamic(trials, size, tolerance)
    

#make_plot(1000, 10, 0.025)