
from abc import ABC, abstractmethod
from point import Point
import random

class ClusterPoint(Point):
    def __init__(self, x, y, cluster):
        super().__init__(x, y)
        self.cluster = cluster

class ClusteringMethods(ABC):
    
    def __init__(self,point_list :list[Point]):
        self.point_list  = point_list
        self.cluster_list = []
        
    
    @abstractmethod    
    def clustering(self):
        """Remplit self.cluster_list avec les groupes de Points."""
        pass
    
    def create_file(self, file_name = "output.txt"):
        tab = "\t"
        with open(file_name, "w") as f:
            for num_cluster,cluster in enumerate(self.cluster_list):
                for point in cluster:
                    f.write(f"{point.x}{tab}{point.y}{tab}{num_cluster}\n")

    def get_cluster_point(self):
        return [ClusterPoint(point.x, point.y, num_cluster)
                for num_cluster, cluster in enumerate(self.cluster_list)
                for point in cluster]
