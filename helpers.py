from flask import Flask, redirect, render_template, Blueprint
import secrets
from pymongo import MongoClient
import os

URI = "mongodb://localhost:27017"


def mongoConnect():
    client = MongoClient(URI)
    try:
        mydb = client["users"]
        mycol = mydb["users"]
        data = {"name": "John", "address": "Highway 37"}
        x = mycol.insert_one(data)
    except Exception:
        print("Unable to connect to the database.")
