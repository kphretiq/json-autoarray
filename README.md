# json_autoarray

Write JSON-serializable python objects to file as JSON array.

Raises a SerializationError if you send it an object that cannot be serialized by whatever json module you are using..
        
Tries to use python-cjson (python2.x only) or UltraJSON  for serializing objects, because you wouldn't be needing a silly thing like this if you weren't handling big old objects.

Objects successfully sent to the writer are always contained in an array. JSONAutoArray will always attempt to close the array upon file closure, regardless of any exceptions which may lead to a premature end of your process.

## Why?

Suppose you are making with the ETL, and are pulling objects from a janky stream. Should your stream close prematurely, or send you some sort of madness, JSONAutoArray will throw out the bad object, and close the array before closing the file. 

## Installation
Install using pip:
```bash
pip install JSONAutoArray
```

## Usage
```python
import random
from json_autoarray import JSONAutoArray

objects = [ 
		{"this": "that"},
		["the", "other"],
		{"hippie": "joe"},
		{
			"facist":{
				"bullyboy":[
					"me",
					"you",
					"them"
					]
			}
		},
		set(["a","a","b"]),
		list(range(3)),
]

f = "foo.json"
with JSONAutoArray.ArrayWriter(f) as writer:
	for obj in objects:
		writer.write(obj)

# will fail in python3 if file opened as binary!
f = open("bar.json", "w")
with JSONAutoArray.ArrayWriter(f) as writer:
	for obj in objects:
		writer.write(obj)

# write ten thousand random flabberdabs
f = "baz.json"
with JSONAutoArray.ArrayWriter(f) as writer:
	try:
		for i in range(10000):
			writer.write([
					{"flabberdab": random.randint(1, 1000)}
				])
	except JSONAutoArray.SerializationError as error:
		print(error)

# close array on StopIteration error
def rando():
	yield set([1,1,1,1,1])
	for i in range(100):
		yield {
				"".join([chr(random.randint(1,100)) for i in range(5)]): \
						random.randint(1,100)}

print("expect uncaught StopIteration")
with JSONAutoArray.ArrayWriter(open("quux.json", "w")) as writer:
	try:
		rg = rando()
		while True:
			if sys.version_info[0] < 3:
				writer.write(rg.next())
			else:
				writer.write(next(rg))
	except JSONAutoArray.SerializationError as error:
		print(error)
```
