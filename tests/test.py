#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import sys
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from json_autoarray import JSONAutoArray
if __name__ == "__main__":
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

    # expect empty array
    f = "bat.json"
    with JSONAutoArray.ArrayWriter(f) as writer:
        try:
            writer.write(lambda x: "foo")
        except JSONAutoArray.SerializationError as error:
            print(error)

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
    def rando_gen():
        yield set([1,1,1,1,1])
        for i in range(100):
            yield {
                    "".join([chr(random.randint(1,100)) for i in range(5)]): \
                            random.randint(1,100)}
    
    print("expect uncaught StopIteration")
    with JSONAutoArray.ArrayWriter(open("quux.json", "w")) as writer:
        try:
            rg = rando_gen()
            while True:
                if sys.version_info[0] < 3:
                    writer.write(rg.next())
                else:
                    writer.write(next(rg))
        except JSONAutoArray.SerializationError as error:
            print(error)


