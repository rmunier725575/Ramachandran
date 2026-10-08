from point import Point
from ClusteringMethods import ClusteringMethods

class Dbscan(ClusteringMethods):


    def __init__(self, point_list: list[Point], epsilon: float,
                 min_points: int, seed=None):
        super().__init__(point_list)
        if epsilon <= 0:
            raise ValueError("epsilon doit être strictement positif.")
        if not isinstance(min_points, int) or min_points < 1:
            raise ValueError("min_points doit être un entier >= 1.")
        self.epsilon = epsilon
        self.min_points = min_points
        self.seed = seed
 
    @staticmethod
    def _distance(a: Point, b: Point) -> float:
        return math.hypot(a.x - b.x, a.y - b.y)


    def _neighbors(self, i: int) -> list[int]:
        p = self.point_list[i]
        return [j for j, q in enumerate(self.point_list)
                if j != i and self._distance(p, q) <= self.epsilon]
 





import random
import math
from Point import Point


class Dbscan(ClusteringMethods):
    NOISE = -1 #étiquette pour les points de bruit


    def __init__(self, points, eps, min_points):
        super().__init__(points)
        self._eps = eps
        self._min_points = min_points
        self._labels = [] #numero de cluster du point i (-1 si bruit)
        self._noise = [] #noise


#accesseurs


def get_eps(self):
    return self._eps


def get_min_points(self):
    return self._min_points


def get_labels(self):
    return self._labels


def get_noise(self):
    return self._noise


#mutateurs


def set_eps(self, eps):
    if eps <= 0:
        raise ValueError("Epsilon must be positive broski")
    self._eps = eps


def set_min_points(self, min_points):
    if min_points < 1:
        raise ValueError("Minimum points must be positive broski")
    self._min_points = min_points


#methodes


def distance(self, point1, point2):
    '''distance euclidiènne entre deux points'''
    return math.sqrt((point1.get_x() - point2.get_x())**2 + (point1.get_y() - point2.get_y())**2)


def neighbors(self, point):
    '''Indices des voisins d'un point donné'''
    neighbors = []
    for p in self.get_points():
        if self.distance(point, p) <= self.get_eps():
            neighbors.append(p)
    return neighbors


def is_core_point(self, point):
    '''Vérifie si un point est un point noyau'''
    return len(self.neighbors(point)) >= self.get_min_points()


def point_type(self, point):
    '''Retourne le type d'un point : "core", "border" ou "noise"'''
    if self.is_core_point(point):
        return "core"
    elif len(self.neighbors(point)) > 0:
        return "border"
    else:
        return "noise"


def cluster(self):
    '''Algorithme DBSCAN pour le clustering des points'''
    self._labels = [None] * len(self.get_points()) #None pas encore visité
    cluster_id = 0


    for i, point in enumerate(self.get_points()):
        if self._labels[i] is not None:
            continue  # Point déjà étiqueté


        if self.is_core_point(point):
            cluster_id += 1
            self.expand_cluster(point, cluster_id)
        else:
            self._labels[i] = Dbscan.NOISE  # bruit marquage


        # construction des résultats
        self._clusters = [[] for _ in range(cluster_id)]
        self._noise = []
        for p, lab in zip(self.get_points(), self._labels):
            if lab == Dbscan.NOISE:
                self._noise.append(p)
            else:
                self._clusters[lab - 1].append(p)  # clusters numérotés à partir de 1
        return self._clusters
 
    # sortie
 
    def write_tsv(self, filename):
        '''Fichier à 3 colonnes : phi, psi, n° de cluster (-1 = bruit)'''
        if not self._labels:
            self.cluster()
        with open(filename, "w") as f:
            for p, lab in zip(self.get_points(), self._labels):
                f.write(f"{p.get_x()}\t{p.get_y()}\t{lab}\n")
