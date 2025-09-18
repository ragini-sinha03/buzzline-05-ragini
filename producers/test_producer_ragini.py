import json
import time

live_data_path = "data/project_live.json"

sample_messages = [
    {
        "message": "Test message 1",
        "author": "Ragini",
        "timestamp": "2025-09-18 10:00:00",
        "category": "test",
        "sentiment": 0.5,
        "keyword_mentioned": "sample",
        "message_length": 15
    },
    {
        "message": "Test message 2",
        "author": "Ragini",
        "timestamp": "2025-09-18 10:01:00",
        "category": "test",
        "sentiment": 0.8,
        "keyword_mentioned": "example",
        "message_length": 15
    }
]

with open(live_data_path, "a") as f:
    for msg in sample_messages:
        f.write(json.dumps(msg) + "\n")
        time.sleep(1)  # Simulate delay between messages

print("Test messages written to live data file.")