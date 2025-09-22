"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    last_but_one_wagon,last_wagon,locomotive,*rest_wagons = each_wagons_id
    final_list_of_wagons = locomotive,*missing_wagons,*rest_wagons,last_but_one_wagon,last_wagon
    return list(final_list_of_wagons)
    

def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route,**more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    first_list,second_list,third_list = wagons_rows
    x1,y1,z1 = first_list
    x2,y2,z2 = second_list
    x3,y3,z3 = third_list
    return[[x1,x2,x3],[y1,y2,y3],[z1,z2,z3]]
