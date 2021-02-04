"""
By Kami Bigdely
Extract Variable (alias introduce explaining variable)
"""

WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """
    Checks if the cooking criteria is satisfied given the time, temp, pressure, and
    desired_state.
    """
    current_state = time * temperature * pressure * COOKED_CONSTANT
    if desired_state == 'well-done' and current_state >= WELL_DONE:
        return True
    if desired_state == 'medium' and current_state >= MEDIUM:
        return True
    return False
