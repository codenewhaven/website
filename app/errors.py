from flask import render_template


def init_errors(app_target):

    @app_target.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', code=404), 404

    @app_target.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', code=500), 500

    @app_target.errorhandler(403)
    def forbidden_error(e):
        return render_template('error.html', code=403), 403

    @app_target.errorhandler(410)
    def gone_error(e):
        return render_template('error.html', code=410), 410
