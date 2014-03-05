# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv

class account_third_check(osv.osv):
    _inherit = "account.third.check"

    def _check_duplicity(self, cr, uid, ids, context=None):
        obj = self.browse(cr, uid, ids[0], context=context)
	bank = obj.bank_id.id
	number = obj.number
	check_ids = self.search(cr,uid,[('bank_id','=',bank),('number','=',number)])

	if len(check_ids) > 1:
		return False	
        return True

    _constraints = [
        (_check_duplicity, 'Checkes duplicados para banco/numero', ['bank_id','number']),
    ]

account_third_check()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
