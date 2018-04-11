class Game:
    """Represents a Discord game.
    Supported Operations:
    +-----------+------------------------------------+
    | Operation |            Description             |
    +===========+====================================+
    | x == y    | Checks if two games are equal.     |
    +-----------+------------------------------------+
    | x != y    | Checks if two games are not equal. |
    +-----------+------------------------------------+
    | hash(x)   | Return the games's hash.           |
    +-----------+------------------------------------+
    | str(x)    | Returns the games's name.          |
    +-----------+------------------------------------+
    Attributes
    -----------
    name: str
        The game's name.
    url: str
        The game's URL. Usually used for twitch streaming.
    type: int
        The type of game being played. 1 indicates "Streaming".
    """

    __slots__ = ['name', 'type', 'url']

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.url = kwargs.get('url')
        self.type = kwargs.get('type', 0)

    def __str__(self):
        return self.name

    def _iterator(self):
        for attr in self.__slots__:
            value = getattr(self, attr, None)
            if value is not None:
                yield (attr, value)

    def __iter__(self):
        return self._iterator()

    def __eq__(self, other):
        return isinstance(other, Game) and other.name == self.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)
