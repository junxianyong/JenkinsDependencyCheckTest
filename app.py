import re
from flask import Flask, render_template, jsonify, request, make_response, session, redirect, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, verify_jwt_in_request
import sqlite3
from datetime import datetime, timedelta
from extensions import db, jwt
from auth import auth_bp
from models import User, TokenBlockList
from users import user_bp
from blog import blog_bp
import os
from flask_migrate import Migrate

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
