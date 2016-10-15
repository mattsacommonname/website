# Copyright 2016 Matthew Bishop
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Entry point."""

import logging
import os
import traceback

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

application = Flask (__name__)

DEBUG = os.environ ['SERVER_SOFTWARE'].startswith ('Development')

application.config.from_object (__name__)

@application.route ('/')
def index ():
    """Index/landing page."""
    output = render_template ('index.html')
    return output

@application.errorhandler (404)
def error_not_found (e):
    """Log the error, display a 404 page."""
    logging.error ('404: "%s"', request.url)
    output = render_template ('404.html')
    return output, 404

@application.errorhandler (418)
def im_a_teapot (e):
    """TODO: Implement brewing protocol."""
    return "I'm a teapot.", 418

@application.errorhandler (500)
def error_server_internal (e):
    """Log the error and stacktrace, inform the user."""
    exc = traceback.format_exc ()
    logging.exception ('500: "%s"\n%s', request.url, exc)
    output = render_template ('500.html')
    return output, 500
