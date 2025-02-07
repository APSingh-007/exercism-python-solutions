def newfunc(route, **kwargs):
    print({**route, "stops": list(kwargs.values())})


newfunc(
    {"from": "New York", "to": "Miami"},
    stop_1="Washington, DC",
    stop_2="Charlotte",
    stop_3="Atlanta",
    stop_4="Jacksonville",
    stop_5="Orlando",
)
