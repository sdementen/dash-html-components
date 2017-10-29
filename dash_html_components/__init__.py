import os as _os
import dash as _dash
import sys as _sys
from .version import __version__

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]

_js_dist = [{
    "relative_package_path": "bundle.js",
    "external_url": (
        "https://unpkg.com/dash-html-components@{}"
        "/dash_html_components/bundle.js"
    ).format(__version__),
    "namespace": "dash_html_components"
}]

_components = _dash.development.component_loader.load_components(
    _os.path.join(_current_path, 'metadata.json'),
    'dash_html_components',
    _js_dist,
)


from .metadata import *