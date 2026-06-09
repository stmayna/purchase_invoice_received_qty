# -*- coding: utf-8 -*-
from odoo import models, _
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare
import logging
_logger = logging.getLogger(__name__)


class PurchaseInvoiceAccountMove(models.Model):
    _inherit = 'account.move'

    def _validate_received_quantity_vendor_bill(self):
        """
        Prevent billing quantity greater than received quantity
        for 3-way matching purchase orders.
        """
        precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure'
        )

        for line in self.invoice_line_ids:
            if (
                line.move_id.move_type != 'in_invoice'
                or not line.purchase_line_id
                # or line.display_type != 'product'
                or line.purchase_line_id.product_id.purchase_method != 'receive'
            ):
                _logger.info("Skipping validation for line %s as it does not meet the criteria.", line.id)

                continue

            po_line = line.purchase_line_id
            allowed_qty = po_line.qty_received

            comparison = float_compare(
                line.quantity,
                allowed_qty,
                precision_digits=precision,
            )

            if comparison > 0:
                raise ValidationError(_(
                    "You cannot bill more than the received quantity.\n\n"
                    "Product: %(product)s\n"
                    "PO: %(po)s\n"
                    "Received Qty: %(received)s\n"
                    "Remaining Qty To Invoice: %(remaining)s\n"
                    "Bill Qty: %(bill_qty)s"
                ) % {
                    'product': line.product_id.display_name,
                    'po': po_line.order_id.name,
                    'received': po_line.qty_received,
                    'remaining': allowed_qty,
                    'bill_qty': line.quantity,
                })

    def action_post(self):
        _logger.info("Starting validation of received quantities for vendor bill %s.", self.name)
        self._validate_received_quantity_vendor_bill()
        _logger.info("Validation successful for vendor bill %s. Proceeding to post.", self.name)
        res = super().action_post()
        return res