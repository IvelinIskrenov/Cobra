from pygame import Vector2, Surface
from base.object import Object

class RenderableObject(Object):
    """
    Abstract base class for game objects that are meant
    to be rendered on the user's screen.

    Parameters:
    sprite - pygame.Surface - sprite that is going to be rendered on;
    the given display;
    position - pygame.Vector2;
    visible - bool.
    """

    def __init__(self,
                 sprite: Surface,
                 position: Vector2 = Vector2(0, 0),
                 visible: bool = True) -> None:
        """
        Initialises renderable object.
        Sets sprite, position and visibility.
        """
        super().__init__(position)
        self.sprite: Surface = sprite
        self.visible: bool = visible

    def is_visible(self) -> bool:
        """Checks if the object is visible"""
        return self.visible

    def make_visible(self) -> None:
        """Makes the object visible"""
        self.visible = True

    def make_invisible(self) -> None:
        """Makes the object invisible"""
        self.invisible = False

    def render(self, display: "Surface") -> None:
        """
        If the object is visible renders the object on it's
        position on the given display
        """
        if self.visible:
            display.blit(self.sprite, self.position)
