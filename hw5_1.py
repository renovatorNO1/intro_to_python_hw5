#****************************
# UNI: yl3433
# Name: Lucas Liu
# Assignment 5
#*****************************


import percolation as perc

def main():
    site_matrix=perc.make_sites(25,0.45)
    perc.write_grid('sites.txt',site_matrix)
    sites_read=perc.read_grid('sites.txt')
    sites_flow=perc.vertical_flow(sites_read)
    if perc.percolates(sites_flow):
        print('percolates')
    else:
        print('does not percolate')


main()
