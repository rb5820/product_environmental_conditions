# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProtectionRating(models.Model):
    _name = 'protection.rating'
    _description = 'Protection Ratings for Products'
    _order = 'sequence, name'
    
    name = fields.Char(
        string='Rating Code',
        required=True,
        help='The code for this protection rating (e.g., IP67, IK08)',
    )
    
    rating_type = fields.Selection([
        ('ip', 'IP - Ingress Protection'),
        ('ik', 'IK - Impact Protection'),
        ('other', 'Other Protection Standard'),
    ], string='Rating Type', required=True, default='ip')
    
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help='Used to order ratings in selection lists',
    )
    
    description = fields.Text(
        string='Description',
        help='Detailed explanation of what this rating means',
    )
    
    first_digit = fields.Char(
        string='First Digit',
        help='For IP ratings: protection against solid objects (0-6)',
    )
    
    second_digit = fields.Char(
        string='Second Digit',
        help='For IP ratings: protection against liquids (0-9)',
    )
    
    first_digit_meaning = fields.Char(
        string='First Digit Meaning',
        help='Description of what the first digit represents',
    )
    
    second_digit_meaning = fields.Char(
        string='Second Digit Meaning',
        help='Description of what the second digit represents',
    )
    
    impact_energy = fields.Float(
        string='Impact Energy (joules)',
        help='For IK ratings: maximum impact energy withstood',
        digits=(6, 2),
    )
    
    standard_reference = fields.Char(
        string='Standard Reference',
        help='Reference to the industry standard that defines this rating',
    )
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Set to false to hide this rating without removing it',
    )
    
    testing_method = fields.Text(
        string='Testing Method',
        help='Description of how products are tested for this rating',
    )
    
    _sql_constraints = [
        ('name_uniq', 'unique(name, rating_type)', 'This rating code already exists for this rating type!')
    ]
