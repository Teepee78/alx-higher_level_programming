#!/usr/bin/python3
"""This module defines the Base class"""
import json
from os import path
import csv
import turtle
from random import random


class Base:
    """A Base class

    Args:
        id: id of instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string represenation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries made from json_string"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = f"{cls.__name__:s}.json"
        write_list = []
        if list_objs is not None:
            for obj in list_objs:
                write_list.append(obj.to_dictionary())
        with open(filename, "w", encoding='utf-8') as f:
            f.write(Base.to_json_string(write_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = f"{cls.__name__:s}.json"

        # check if file doesn't exist
        if path.exists(filename) is False:
            return []

        with open(filename, "r", encoding='utf-8') as f:
            instances = []
            # create list of dictionaries
            json = cls.from_json_string(f.read())

            for dic in json:
                instances.append(cls.create(**dic))

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""

        # write filename
        filename = f"{cls.__name__:s}.csv"
        # create list of dictionaries of objects to be written
        write_list = []
        if list_objs is not None:
            for obj in list_objs:
                write_list.append(obj.to_dictionary())
        # create field names
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        # write file
        with open(filename, "w", encoding='utf-8') as f:
            # create dict writer object
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            # write each row
            for row in write_list:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""

        filename = f"{cls.__name__:s}.csv"

        # check if file doesn't exist
        if path.exists(filename) is False:
            return []

        with open(filename, "r", encoding='utf-8') as f:
            csv_file = csv.DictReader(f)
            instances = []

            for dic in csv_file:
                # cast each field to the appropriate type
                for key, value in dic.items():
                    dic[key] = int(value)
                instances.append(cls.create(**dic))

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares
        Screen set to 200 x 150 - best width/height ratio for correct display
        Parameters:
            list_rectangles: list of rectangles to draw
            list_squares: list of squares to draw
        """

        width, height = 200, 150
        ts = turtle.getscreen()
        turtle.screensize(width, height)
        turtle.setworldcoordinates(0, 0, width, height)
        turtle.pensize(5)
        shapes = list_rectangles + list_squares
        for shape in shapes:
            fill_color = (random(), random(), random())
            pen_color = (random(), random(), random())
            turtle.color(fill_color, pen_color)
            turtle.setpos((shape.x, shape.y))
            turtle.down()
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(shape.height)
                turtle.left(90)
                turtle.forward(shape.width)
                turtle.left(90)
            turtle.end_fill()
            turtle.up()
        ts.exitonclick()
