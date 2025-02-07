"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0

    def __init__(self, x_pos, y_pos) -> None:
        self.x_coordinate, self.y_coordinate = x_pos, y_pos
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        self.health -= 1

    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        return True

    def teleport(self, *new_coordinates) -> None:
        self.x_coordinate, self.y_coordinate = new_coordinates

    def collision_detection(self, other) -> bool:
        pass


# function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions: list) -> list:
    """
    param alien_start_positions: list - List containing tuples of starting position of new aliens to be created
    returns - list of objects of Alien class
    """
    alien_train = []
    for x_pos, y_pos in alien_start_positions:
        alien_train.append(Alien(x_pos, y_pos))
    return alien_train
