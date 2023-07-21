from pygame import Vector2

class GameObject():
    """
    Abstract base class for all game objects that are positionable.

    parameteres:
    position - pygame.Vector2
    """

    def __init__(self, 
                 position: "Vector2" = Vector2(0, 0)) -> None:
        """
        Initialises the game object.
        Sets sposition.
        """
        self.position = position

    def get_position(self) -> Vector2:
        """Returns the current poisiton of the object"""
        return self.position