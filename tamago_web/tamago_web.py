import coloredlogs
import logging
import flask
from waitress import serve
from tamago_web.lib import utils

LOG = logging.getLogger(__name__)
app = flask.Flask('Tamgao-Web')

@app.after_request
def web_logger(response):
    """
    log_the_status_code - prints logging status after every request
    param obj response: the response from a route for logging
    """
    LOG.info('%s %s %s %s', flask.request.remote_addr, flask.request.method,
                    flask.request.full_path, response.status)
    return response

@app.route('/')
def home():
    return flask.render_template('home.html')

def main():
    """Entrypoint if called as an executable."""
    args = utils.parse_arguments()
    logging.basicConfig(level=logging.INFO)
    coloredlogs.install(level=0,
                        fmt="[%(asctime)s][%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                        isatty=True)
    if args.debug:
        l_level = logging.DEBUG
    else:
        l_level = logging.INFO

    logging.getLogger(__package__).setLevel(l_level)

    LOG.info('RUNNING TAMAGO WEB')
    serve(app, port=8080, host='0.0.0.0')

if __name__ == '__main__':
    main()
