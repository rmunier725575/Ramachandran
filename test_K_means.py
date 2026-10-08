from Kmeans import Kmeans
from Point import Point


def test_k():
    points = [Point(0, 0), Point(1, 1)]
    kmeans = Kmeans(points, 2)

    assert kmeans.k == 2


def test_set_k():
    points = [Point(0, 0), Point(1, 1)]
    kmeans = Kmeans(points, 2)

    kmeans.k = 3

    assert kmeans.k == 3


def test_points():
    points = [Point(0, 0), Point(1, 1)]
    kmeans = Kmeans(points, 2)

    assert kmeans.point_list == points


def test_empty_points():
    kmeans = Kmeans([], 2)

    assert kmeans.point_list == []


def test_kmeans_function():
    points = [
        Point(0, 0),
        Point(1, 1),
        Point(10, 10),
        Point(11, 11)
    ]

    kmeans = Kmeans(points, 2)

    clusters = kmeans.kmeans_function()

    assert len(clusters) == 2


def test_clustering():
    points = [
        Point(0, 0),
        Point(1, 1),
        Point(10, 10),
        Point(11, 11)
    ]

    kmeans = Kmeans(points, 2)

    result = kmeans.clustering()

    assert len(result) == 2


