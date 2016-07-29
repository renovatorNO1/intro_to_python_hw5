# *******************************************************
# Name: Lucas Liu
# UNI: yl3433
# hw5b module
# Assignment 5 Part 2
# ENGI E1006
# *******************************************************


import percolation2 as perc



def main():
    A=perc.make_sites(20,0.6)
    perc.write_grid('sites.txt',A)
    B=perc.read_grid('sites.txt')
    C=perc.undirected_flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    
    #visualize flow
    perc.show_perc(B)

    #generate percolation probability graph
    #perc.make_plot(10,5000)

main()
