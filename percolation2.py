# *******************************************************
# Name: Lucas Liu
# UNI: yl3433
# hw5b module
# Assignment 5 Part 2
# ENGI E1006
# *******************************************************


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def read_grid(infile_name):
    """Create a site vacancy matrix from a text file.

    infile_name is the name (a string) of the
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    in_file = open(infile_name, 'r')
    count = 0 #set up a counter for lines in in_file
    vacant_sites = [] #create a local variable out_file 
    # read the in_file
    for line in in_file:
        count += 1
        #if the count is greater than 1, then split the line into a list and 
        # append it into out_file
        if count > 1:
            row = line.split()
            vacant_sites.append(row)
    #set out_file as a np array
    vacant_sites = np.array(vacant_sites)
    #change every element in the out_file into an integer
    vacant_sites = vacant_sites.astype(int)
    in_file.close()
    
    return (vacant_sites)


def write_grid(outfile_name,sites):
    """Write a site vacancy matrix to a file.

    filename is a string that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    out_file = open(outfile_name, 'w') #open the out_file in write mode 
    N = sites.shape[0] # store the #of row into variable N
    out_file.write(str(N)+'\n') #write N on the first line
    
    #write every row on a new line in the out_file
    for row in sites:
        a = " ".join(row.astype(str)) + "\n"
        out_file.write(a)
    
    out_file.close()


def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """
    #Make a flow_sites with the same dimension as the sites
    flow_sites = np.zeros(sites.shape)
    flow_sites = flow_sites.astype(int)
    
    #Start the Percolation from the first line 
    for k in range(sites.shape[0]):
        flow_from(sites,flow_sites,0,k)
       
    return flow_sites
            
def flow_from(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    if i in range(sites.shape[0]) and j in range(sites.shape[0]):

        #Check if the site is open and vacant 
        if sites[i,j] == 1 and full[i,j] == 0:
            full[i,j] = 1
            
            #Check the right site
            flow_from(sites, full, i, j+1)
            #Check the left site
            flow_from(sites, full, i, j-1)
            #Check the lower site
            flow_from(sites, full, i+1, j)
            #Check the upper site
            flow_from(sites, full, i-1, j)

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    last_row  = sum(flow_matrix[-1])
    
    # if last_row is 0, then return False; if it's greater than 0, then return Ture
    return True if last_row else False

def make_sites(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    #Construct an n*n array 
    array_rand = np.random.rand(n**2)
    array_rand.resize(n,n)
    
    #turn the randomized array into an array with boolean values
    # if the element < p, then change the element into Ture
    array_rand = array_rand<p
    #Change the elements of array_rand into integers
    array_rand = array_rand.astype(int)
    
    return array_rand

def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    # Create the sites to be visualized as the sum of the other two sites
    sites_undirected = undirected_flow(sites)
    sites_visualized = sites_undirected + sites
   
    # set the colormap with red = 0, black = 1, blue = 2
    cmap = colors.ListedColormap(['red','black','blue'])
    
    #numbers in bounds determine the color's transitioning point 
    bounds = [-.5, .5,1.5,3]   
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    plt.matshow(sites_visualized, cmap=cmap, norm=norm)

def make_plot(n,trials):
    """generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for directed 
    percolation by running a Monte Carlo simulation using the variable trials number
    of trials for each point. 
    """
    #p_vacancy makes up the x-axis
    p_vacancy = np.linspace(0, 1, 100)
    
    #p_perpercolation makes up the vertical values
    p_percolation = np.zeros(100)
    
    #For every probability in p_vacancy
    for p in range(len(p_vacancy)):
        
        #Initiate the count of success
        success = 0       
        #Execute all the trials
        for x in range(trials):
            
            #Construct a vacant site with vacancy probability as p
            array_vacancy = make_sites(n, p_vacancy[p])
            
            #Yield full site after the vacant site goes through undirected percolation
            array_percolation = undirected_flow(array_vacancy)
            
            #Increment count of success by 1 if it percolates
            if percolates(array_percolation):
                success += 1
        #Calculate the success rate by taking the ratio of #of success to #of trials        
        success_rate = float(success/trials)
        #Append each success rate into the p_percolation as the vertical values of the graph
        p_percolation[p] = success_rate
    
    #Plot the graph    
    plt.figure(0)
    plt.plot(p_vacancy,p_percolation)

            

