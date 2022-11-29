from flask import Flask
from jinja2_markdown import MarkdownExtension
from flask_wtf.csrf import CSRFProtect
import sys
import logging

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)
csrf = CSRFProtect(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s;%(module)s;%(funcName)s;%(levelname)s;%(message)s')
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
fh = logging.FileHandler('portal.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

if len(sys.argv) > 1:
    try:
        config_file = sys.argv[1]
        app.config.from_pyfile(config_file)
        logger.info("Loaded portal.conf from %s" %config_file)
    except:
        logger.error("Unable to load portal.conf from %s" %sys.argv[1])
else:
    app.config.from_pyfile("../secrets/portal.conf")
    logger.info("Loaded portal.conf from ../secrets/portal.conf")

import portal.views