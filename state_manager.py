current_state = "idle"

def set_state(state):

    global current_state

    current_state = state

    print(f"\nSTATE -> {state}")

def get_state():

    return current_state