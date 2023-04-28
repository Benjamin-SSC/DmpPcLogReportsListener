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

        # If the returned field is an Event Type, this info is stored as keys in the dict
        if parsedField['fieldtype'] == 't' and not 't' in message_dict.keys():
            message_dict['event_type'] = parsedField['event_type']
            message_dict['event_qualifier'] = parsedField['qualifier']
            message_dict['event_istext'] = parsedField['istext']
        elif parsedField['fieldtype'] == 't' and not 't' in message_dict.keys():
            # WTFOMGBBQ - WE SHOULD NOT BE HERE!
            print(f"I'VE RECEIEVED A SECOND EVENT TYPE FOR THE SAME SIGNAL!!! WE SHOULD NOT BE HERE! I'M QUITTING!")
            quit()
        else:
             # If it's any other type, we add it to a list under the key of it's type.
            if not parsedField['fieldtype'] in message_dict.keys():
                 message_dict[parsedField['fieldtype']] = []
            message_dict[parsedField['fieldtype']] += [parsedField]

    print(json.dumps(message_dict, indent=2))

    return message_dict

# Parse a field, and then handle it by type
def parseField(field:str):
    field_dict = {}

    # The first char of the field tells us what it is. I'll call this the field identifier.
    field_ident = field[0]
    field = field[1:]

    match field_ident:
        case "a":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "b":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "c":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "d":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "e":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "g":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "h":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "i":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "n":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "p":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "s":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
        case "t":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
            field_dict = parseEventType(field)
        case "u":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
            field_dict = parseUser(field)
        case "v":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
            field_dict = parseDevice(field)
        case "z":
            dmputils.debugPrint(f"Processing '{field_ident}' as '{dmpstaticdata.field_ident_map[field_ident]}' Field")
            field_dict = parseZone(field)
        case _:
            print(f"ERROR: Unknown Field '{field_ident}'")

    return field_dict

# Parse the zone (z) field
def parseZone(field:str):
    field_dict = {}
    field_dict['fieldtype'] = "z"
    return field_dict

# Parse a Device (v) field. Return dict
def parseDevice(field:str):
    field_dict = {}
    field_dict['fieldtype'] = "v"
    field_dict['qualifier'] = field[0]
    split = field[1:].split("\"")
    field_dict['identifier'] = split[0]
    field_dict['text'] = split[1]
    return field_dict

# Parse a User (u) field. Return dict
def parseUser(field:str):
    field_dict = {}
    field_dict['fieldtype'] = "u"
    field_dict['qualifier'] = field[0]
    split = field[1:].split("\"")
    field_dict['identifier'] = split[0]
    field_dict['text'] = split[1]
    return field_dict

# Parse the Event Type (t) field. Return dict. This one is special.
def parseEventType(field:str):
    istext = False
    if field[1] == '"':
        istext = True
        eventtype = field[2:]
    else:
        eventtype = field[1:]

    field_dict = {}
    field_dict['fieldtype'] = "t"
    field_dict['qualifier'] = field[0]
    field_dict['event_type'] = eventtype
    field_dict['istext'] = str(istext)
    return field_dict

# EOF
