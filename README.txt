This project has two files. hw5_2.py and percolation2.py
The percolation.py file contains all the functions needed.

Explanations for my design:
for the flow_from function:
I use recursive call in this function because it silmuates precisely the motion of water. If the site qualifies 
for being filled with water, then go to the sites near it and check whether it is vacant. If its vacant, then 
fill it out as well and check the sites nearby. Repear the process untill all the qualified vacant sites are filled 
out with water.

For the matrix image:
I use blue color to represent full sites, black color to represent vacant sites, and red color to represent blocked
sites. Each color correspons to a specific number.

For the plotting:
I know it takes about 4 minutes to run. Sorry about that slowness. But I think it is necessary to iterate sufficient times in order to plot an accurate graph. There are approximately 100 points in the graph.

percolation2.py is imported as a module in hw5_2.py.
Run the hw5_1.py file in python compiler and you will see the results. Thank you! 
