#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import sae
from home import app

root = os.path.dirname(__file__)

# 两者取其一
sys.path.insert(0, os.path.join(root, 'site-packages'))

application = sae.create_wsgi_app(app)
