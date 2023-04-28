### Holds static data like long dicts ###

# This maps the first letter of a field to a description of some kind
field_ident_map = {
    "a" : "Area",
    "b" : "Signal Strength",
    "c" : "Path (Communication) Information",
    "d" : "Date",
    "e" : "Event Qualifier",
    "g" : "Equipment ID",
    "h" : "Holiday",
    "i" : "Time/Day",
    "n" : "Schedule Name",
    "p" : "Programming",
    "s" : "Service Code",
    "t" : "Event Type",
    "u" : "User Code",
    "v" : "Device",
    "z" : "Zone"
}

# Generate some english for the event definition
event_def_map = {
    "a" : "Zone Alarm",
    "b" : "Zone Force Alarm",
    "c" : "Real-Time Status",
    "d" : "Wireless Zone Low Battery (LOWBAT)",
    "e" : "Equipment (hardware receivers)",
    "f" : "Zone Fail",
    "g" : "Holidays",
    "h" : "Wireless Zone Missing",
    "i" : "Zone Tamper",
    "j" : "Door Access",
    "k" : "Walk Test Zone Verify",
    "l" : "Schedules",
    "m" : "Service Code",
    "p" : "Zone Trip Count",
    "q" : "Arming Status",
    "r" : "Zone Restore",
    "s" : "System Message",
    "t" : "Zone Trouble",
    "u" : "User Codes",
    "w" : "Zone Fault",
    "x" : "Zone Bypass",
    "y" : "Zone Reset",
    "z" : "Reserved Type (System Use Only)"
}

# EOF
