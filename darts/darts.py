def score(x, y) -> int:
    """
    Since the centre of the dart board is at origin(0,0), we can calculate the distance of dart(x,y) from centre,
    to find which circle the dart landed on. This can be found by the equation distance = sqrt(x^2 +y^2)
    """
    distance = pow((x**2 + y**2), 0.5)
    point_system = {1: 10, 5: 5, 10: 1}

    for radius, points in point_system.items():
        if distance <= radius:
            return points
    return 0
