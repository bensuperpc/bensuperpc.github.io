from sys import prefix

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from loguru import logger

from .db import db

admin = Blueprint(
    "admin",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/",
)


@admin.route("/admin")
@login_required
def main_admin():
    if current_user.admin is False:
        flash("Sorry, you don't have permission to access the admin panel.")
        logger.warning(
            f"User {current_user.name} ({current_user.email}) tried to log access admin panel"
        )
        return redirect(url_for("main.index"))

    return render_template("admin.html")
