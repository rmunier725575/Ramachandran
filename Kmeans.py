from point import Point
from ClusteringMethods import ClusteringMethods
class Kmeans(ClusteringMethods):
    def __init__(self, point_list, k_value):
        super().__init__(point_list)
        self.k = k_value


    def clustering(self):
        self.cluster_list = self.kmeans_function()
        return self.cluster_list


    @property
    def k(self):
        return self._k


    @k.setter
    def k(self, value):
        self._k = value


    def kmeans_function(self):
        ### Premiers centroides aléatoires
        centroid = random.sample(self.point_list, k=self.k)
        stable = False
        while not stable:
            ### Placement des points dans le groupe du centroide le plus proche
            clusters = [[] for _ in centroid]
            for point in self.point_list:
                i_proche = min(range(len(centroid)), key=lambda i: point.euclidean_distance(centroid[i]))
                clusters[i_proche].append(point)
            ### Calcul des nouveaux centroides (moyenne des points du groupe)
            new_centroid = []
            for i in range(len(clusters)):
                c = clusters[i]
                if len(c) == 0:  # groupe vide : on garde l'ancien centroide
                    new_centroid.append(centroid[i])
                    continue
                somme_x = 0
                somme_y = 0
                for p in c:
                    somme_x += p.get_abs()
                    somme_y += p.get_ord()
                new_centroid.append(Point(somme_x / len(c), somme_y / len(c)))
            ### On s'arrête quand les centroides ne bougent plus
            stable = True
            for i in range(len(centroid)):
                if centroid[i].euclidean_distance(new_centroid[i]) > 1e-6:
                    stable = False
            centroid = new_centroid
        return clusters
