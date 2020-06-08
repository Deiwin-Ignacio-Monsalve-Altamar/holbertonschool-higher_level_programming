#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    json_example = Base.to_json_string(None)
    print(type(json_example))
    print(json_example)

