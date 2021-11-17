# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
from odoo.tools import float_is_zero, float_compare, safe_eval, date_utils, email_split, email_escape_char, email_re
from odoo.tools.misc import formatLang, format_date, get_lang

from collections import defaultdict
from datetime import date, timedelta
from itertools import groupby
from itertools import zip_longest
from hashlib import sha256
from json import dumps

import json
import re

class HnAccountJournalInherit(models.Model):
    _inherit = "account.journal"

    debit_note_sale = fields.Boolean(string="Nota de debito(Venta)",  tracking=True)
    debit_note_purchase = fields.Boolean(string="Nota de debito(Compra)",  tracking=True)


