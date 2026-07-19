conversation_memory = []

MAX_MEMORY = 10

def add_memory(role, content):

    # ignore empty memory
    if not content:
        return

    content = content.strip()

    # ignore tiny junk
    if len(content) < 3:
        return

    conversation_memory.append({

        "role": role,
        "content": content
    })

    # keep latest memory only
    if len(conversation_memory) > MAX_MEMORY:

        conversation_memory.pop(0)

def get_memory():

    return conversation_memory

def clear_memory():

    conversation_memory.clear()