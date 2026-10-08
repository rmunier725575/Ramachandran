
import pytest
from Dbscan import Dbscan
from Point import Point


def test_get_eps():
    points = [Point(0, 0), Point(1, 1)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.get_eps() == 2


def test_get_min_points():
    points = [Point(0, 0), Point(1, 1)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.get_min_points() == 3


def test_get_labels():
    points = [Point(0, 0), Point(1, 1)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.get_labels() == []


def test_get_noise():
    points = [Point(0, 0), Point(1, 1)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.get_noise() == []


def test_set_eps():
    points = [Point(0, 0)]
    dbscan = Dbscan(points, 2, 3)

    dbscan.set_eps(5)

    assert dbscan.get_eps() == 5


def test_set_min_points():
    points = [Point(0, 0)]
    dbscan = Dbscan(points, 2, 3)

    dbscan.set_min_points(5)

    assert dbscan.get_min_points() == 5


def test_set_eps_error():
    points = [Point(0, 0)]
    dbscan = Dbscan(points, 2, 3)

    with pytest.raises(ValueError):
        dbscan.set_eps(0)


def test_set_min_points_error():
    points = [Point(0, 0)]
    dbscan = Dbscan(points, 2, 3)

    with pytest.raises(ValueError):
        dbscan.set_min_points(0)


def test_distance():
    points = [Point(0, 0), Point(3, 4)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.distance(points[0], points[1]) == 5


def test_distance_zero():
    points = [Point(0, 0)]
    dbscan = Dbscan(points, 2, 3)

    assert dbscan.distance(points[0], points[0]) == 0


def test_neighbors():
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(5, 5)

    dbscan = Dbscan([p1, p2, p3], 1.5, 2)

    result = dbscan.neighbors(p1)

    assert p2 in result
    assert p3 not in result