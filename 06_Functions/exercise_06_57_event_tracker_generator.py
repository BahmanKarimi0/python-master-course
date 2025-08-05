def event_tracker(events):
    for count, event in enumerate(events, 1):
        yield f'[{count}] Received event: {event}'


events = ["Login", "ViewProfile", "Logout"]
gen = event_tracker(events)
for log in gen:
    print(log)