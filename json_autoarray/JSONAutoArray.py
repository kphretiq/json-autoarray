#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convenience module to "stream" json-serializable python objects into an array,
automatically bound array on file open and close

supports python-cjson (python2.x) or UltraJSON for writing, because C.

initialize with file object or filename

 Usage:
        from json_autoarray import JSONAutoArray

        f = "foo.json" # or file-like object
        with JSONAutoArray.ArrayWriter(f) as mystream:
            mystream.write({"this": "that"})
            mystream.write({"the": "other"})
            mystream.write({"hippie": "joe"})
            mystream.write({"facist":{"bullyboy":["me", "you", "them"]}})
        
"""

import sys
import warnings
from io import IOBase

try:
    import cjson as json
    json.dumps = json.encode
except ImportError:
    # cjson not yet supported by python3, try UltraJSON
    try:
        import ujson as json
    except ImportError:
        import json

class ArrayWriter(object):
    """
    accepts a file path or a file like object
    writes the output as a json array
    in file

    """
    def __init__(self, o):

        if sys.version_info[0] < 3:
            if isinstance(o, file):
                self.obj = o
        else:
            if isinstance(o, IOBase):
                self.obj = o

        if isinstance(o, str):
            self.obj = open(o, "w")

    def __enter__(self):
        """
        bound input with open square bracket
        """
        self.obj.write("[")
        return self

    def __exit__(self, _type, value, traceback):
        """
        bound input with close square bracket, then close the file
        """
        self.obj.write("]")
        self.obj.close()

    def write(self, obj):
        """
        writes the first row, then overloads self with delimited_write
        """
        try:
            self.obj.write(json.dumps(obj))
            setattr(self, "write", self.delimited_write)
        except:
            self.bad_obj(obj)

    def delimited_write(self, obj):
        """
        prefix json object with a comma
        """
        try:
            self.obj.write("," + json.dumps(obj))
        except:
            self.bad_obj(obj)

    def bad_obj(self, obj):
        raise SerializationError("Object not serializable")
 
class SerializationError(Exception):
    def __init__(self, value):
        self.value = value 

    def __str__(self):
        return repr(self.value) 
