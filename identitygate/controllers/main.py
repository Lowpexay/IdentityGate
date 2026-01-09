from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ..models import Module
from ..services.access_control import require_access


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def dashboard():
    modules = Module.query.order_by(Module.name.asc()).all()
    return render_template("dashboard.html", modules=modules)


@main_bp.route("/module/<module_code>")
@login_required
@require_access(module_code="dynamic")
def module_view(module_code: str):
    # The decorator is parameterized dynamically; handled within decorator logic.
    # This route renders a simple module page.
    module = Module.query.filter_by(code=module_code).first()
    return render_template("module.html", module=module)
