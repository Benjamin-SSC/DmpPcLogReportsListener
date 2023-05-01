### Helper parsing functions for dmp-listener ###
import json
from dmplib import dmputils
from dmplib import dmpstaticdata

# Parse Message into fields. Return Dict
def parseMessage(msg_list:list):

    message_dict = {}

    # All message strings must start with a 'Z'
    if msg_list[0][0] != 'Z':
        print("This message doesn't seem valid. It doesn't start with 'Z'")
        return False

    # Break out the event definition. It's *always* the 2nd char in the message
    message_dict['event_definition'] = msg_list[0][1]

    # Save the message length just in case we need it some time
    message_dict['length'] = msg_list[1]

    # Remove the first two items from the list. We parse the rest iteratively
    del msg_list[:2]

    # Loop though the rest of the fields, and handle them
    for msg_field in msg_list:
        if not msg_field: # Skip empty fields... like the last one.
           continue

        parsedField = parseField(msg_field)

        # We add it to a list under the key of it's type.
        if not parsedField['fieldtype'] in message_dict.keys():
            message_dict[parsedField['fieldtype']] = []
        message_dict[parsedField['fieldtype']] += [parsedField]

    return message_dict

# Parse a field, and then handle it by type
def parseField(field:str):
    field_dict = {}

    # The first char of the field tells us what it is. I'll call this the field identifier.
    field_ident = field[0]
    field = field[1:]

    event_desc = dmpstaticdata.field_ident_map.get(field_ident)
    if event_desc:
        dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
    else:
        print(f"WARNING: Field Identifier '{field_ident}' is not defined!")

    field_dict['fieldtype'] = field_ident
    field_dict['qualifier'] = field[0]
    split = field[1:].split("\"")
    field_dict['identifier'] = split[0]

    if len(split) == 2:
        field_dict['text'] = '"'.join(split[1:])
    else:
        field_dict['text'] = ""

    return field_dict

# EOF
