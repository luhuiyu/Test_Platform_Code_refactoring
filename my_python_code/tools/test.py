import records

rows = [
    {"x": 1, "y": 2},
    {"x": 2, "y": 3},
    {"x": 3, "y": 4},
    {"x": 4, "y": 9}
]
results = records.RecordCollection(iter(rows))
with open('demo.xls', 'wb') as f:
    f.write(results.export('xlsx'))