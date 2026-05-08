conversation_memory = []

MAX_MEMORY = 10

def add_memory(role, content):

    conversation_memory.append({

        "role": role,
        "content": content
    })

    # keep latest messages only
    if len(conversation_memory) > MAX_MEMORY:

        conversation_memory.pop(0)

def get_memory():

    return conversation_memory