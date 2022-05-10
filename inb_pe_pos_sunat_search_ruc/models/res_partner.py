# -*- coding: utf-8 -*-
##-----------------------------------------------------------------------------##
#
#    Copyright (C) 2021-TODAY Inbrasol.
#    Author      :  Inbrasol S.A.C.
#    WebSite     : https://www.inbrasol.pe
#
#    This program is copyright property of the author mentioned above.
#    You can't redistribute it and/or modify it.
#
##-----------------------------------------------------------------------------##
from requests.models import Response
from odoo import models, fields, api, _
import requests
import json


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _default_country(self):
        return self.env.company.country_id.id