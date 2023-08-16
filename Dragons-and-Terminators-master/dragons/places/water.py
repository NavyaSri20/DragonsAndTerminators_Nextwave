from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""

    def add_fighter(self, fighter):
        """Add a Fighter to this place. If the fighter is not watersafe, reduce
        its armor to 0."""
        # BEGIN 4.1
        "*** YOUR CODE HERE ***"
        # Firstly add fighter irrespective of water safe or not
        Place.add_fighter(self, fighter)

        # If fighter is not watersafe, reduce armor to 0
        if fighter.is_watersafe == False:
            fighter.reduce_armor(fighter.armor)