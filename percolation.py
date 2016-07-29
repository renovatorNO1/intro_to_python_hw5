##############################
# UNI: yl3433
# Name: Lucas Liu
# Assignment5
#####################

import numpy as np


def read_grid(infile_name):
    """Create a site vacancy matrix from a text file.

    infile_name is the name (a string)  of the
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
    
    
    ### your code here ###
 
def write_grid(outfile_name,sites):
    """Write a site vacancy matrix to a file.

    outfile_name is a string that is the name of the
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
 
def vertical_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through vertical percolation
    """
    #Make a copy of the sites
    sites_flow = sites
    
    #Iterate from the second line of sites
    for x in range(1, sites.shape[0]):
        for i in range(len(sites[x])):
            #mark the site as full if it's an open site(1) and the site above it is full(1)
            if sites[x,i] == 1 and sites[x-1, i] == 1:
                sites_flow[x,i] = 1 
                
            #Otherwise mark it vacant
            else:
                sites_flow[x,i] = 0
                
    #Format the sites_flow into an array of 0 and 1
    sites_flow = sites_flow.astype(int)
    return sites_flow
            
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
    #create a randomized array with n*n dimension
    array_rand = np.random.rand(n**2)
    array_rand.resize(n,n)
    
    #turn the randomized array into an array with boolean values
    # if the element < p, then change the element into Ture
    array_rand = array_rand<p
    #Change the elements of array_rand into integers
    array_rand = array_rand.astype(int)
    
    return array_rand
