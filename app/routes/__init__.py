from app.routes.auth import auth
from app.routes.panel import panel
from app.routes.main import main

blueprints = [
    auth,
    panel,
    main
]