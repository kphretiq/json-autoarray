# json_autoarray

Write JSON-serializable python objects to file as JSON array.

Raises a SerializationError if you send it an object that cannot be serialized by whatever json module you are using..
        
Tries to use python-cjson (python2.x only) or UltraJSON  for serializing objects, because you wouldn't be needing a silly thing like this if you weren't handling big old objects.

Objects successfully sent to the writer are always contained in an array. JSONAutoArray will always attempt to close the array upon file closure, regardless of any exceptions which may lead to a premature end of your process.

## Why?

Suppose you are making with the ETL, and are pulling objects from a janky stream. Should your stream close prematurely, or send you some sort of madness, JSONAutoArray will throw out the bad object, and close the array before closing the file. 

Usage:
```python
import json_autoarray.JSONAutoaArray as JSONAutoaArray

f = "foo.json" # or file-like object
with JSONAutoaArray.ArrayWriter(f) as writer:
	writer.write({"this": "that"})
	writer.write({"the": "other"})
	writer.write({"hippie": "joe"})
	writer.write({"facist":{"bullyboy":["me", "you", "them"]}})


[
	{
		"this": "that"
	},
	[
		"the",
		"other"
	],
	{
		"hippie": "joe"
	},
	{
		"facist": {
			"bullyboy": [
				"me",
				"you",
				"them"
			]
		}
	},
	[
		"a",
		"b"
	],
	[
		0,
		1,
		2
	]
]
```
