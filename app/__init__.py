from flask import Flask, jsonify
from flask_restful import Api

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.characters.api_v1_0.resources import crews_v1_0_bp
from .ext import ma, migrate