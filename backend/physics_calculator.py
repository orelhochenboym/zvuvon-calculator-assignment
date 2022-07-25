from cmath import tan
import math

# Earth's gravity. The value is negative because gravitational force draws a body downwards.
G = -9.8


def calculate_info(starting_velocity, starting_angle, starting_height):
    """
        The grids are set so the root (0, 0) is the location that the plane is directly above.
        for example: if the plane's altitude is 500m at the moment of dropping the bomb,
        its location on the grid is (0, 500).

        When we are calculating the zvovun's trajectory, we are looking at the plane carrying directly from behind.
        Which means that the only angles possible range from directly going up, which means 90 degrees, to directly
        going down, which means -90 degrees.
        In short, our domain is -90 < angle < 90 degrees.
    """

    starting_velocity = float(starting_velocity)
    starting_angle = float(starting_angle)
    starting_height = float(starting_height)

    # The velocity at the moment of dropping the bomb on the x axis (horizontal speed).
    starting_x_velocity = starting_velocity * \
        math.cos(math.radians(starting_angle))

    # The velocity at the moment of dropping the bomb on the y axis (vertical speed).
    starting_y_velocity = starting_velocity * \
        math.sin(math.radians(starting_angle))

    # Time it takes the bomb to hit the ground.
    time_until_impact = solve_for_2nd_degree(
        a=G / 2, b=starting_y_velocity, c=starting_height)

    if starting_velocity == 0:
        return {'hit_position': 0, 'hit_velocity': starting_velocity + -G * time_until_impact, 'hit_angle': 90}
    elif starting_height == 0:
        return {'hit_position': 0, 'hit_velocity': starting_velocity, 'hit_angle': starting_angle}

    # The position of the bomb on the x axis (because y = 0 -> 0 is the ground) at impact.
    hit_position = time_until_impact * starting_x_velocity

    # The bomb's velocity at impact.
    hit_velocity = math.hypot(
        starting_x_velocity, starting_y_velocity + G * time_until_impact)

    # The bomb's angle of impact at impact (not the angle of the bomb iself relative to the ground, but it's trajectory's angle relative to the ground).
    if starting_x_velocity == 0:
        hit_angle = starting_angle
    else:
        hit_angle = math.degrees(math.atan2(
            abs(starting_y_velocity + G * time_until_impact), starting_x_velocity))

    return {'hit_position': hit_position, 'hit_velocity': hit_velocity, 'hit_angle': hit_angle}


def solve_for_2nd_degree(a, b, c):
    delta = b**2 - 4 * a * c

    if delta < 0:
        return -1
    else:
        sqrt = math.sqrt(delta)
        x1 = (-b + sqrt) / (2.0 * a)
        x2 = (-b - sqrt) / (2.0 * a)
        if x1 == x2:
            return x1
        else:
            return max(x1, x2)
