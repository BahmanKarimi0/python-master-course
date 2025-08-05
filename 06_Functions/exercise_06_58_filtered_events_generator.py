from typing import Generator


def filtered_events(events:list[str], important:list[str]) -> Generator[str, None, None]:
    for event in events:
        if event in important:
            yield event


events = ["Login", "ViewProfile", "Logout", "Download", "Error", "Upload"]
important = ["Login", "Logout", "Error"]

gen = filtered_events(events, important)
for log in gen:
    print(log)