import pandas as pd 
import numpy as np 


class kmean :
    def __init__(self , n_clusters=3 , max_iter=100 , tol=1e-4 , random_state=None , init="kmeans++"):
        self.n_clusters=3,
        self.max_iter=100,
        self.tol=1e-4,
        self.random_state=42,
        self.init="kmeans++",
        self.cluster_centre = None,
        self.labels = None,
        self.intertia = None

        if random_state is not None :
            np.random.seed(random_state)

    def euclidian_distance(self , X , center):
        
      
