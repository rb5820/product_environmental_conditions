# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    # Temperature specifications
    min_operating_temp = fields.Float(
        string='Min Operating Temperature (°C)',
        help='Minimum temperature at which the product can safely operate',
        tracking=True,
        default=None,
        digits=(5, 2),
    )
    
    max_operating_temp = fields.Float(
        string='Max Operating Temperature (°C)', 
        help='Maximum temperature at which the product can safely operate',
        tracking=True,
        digits=(5, 2),
    )
    
    min_storage_temp = fields.Float(
        string='Min Storage Temperature (°C)',
        help='Minimum temperature at which the product can be safely stored',
        tracking=True,
        digits=(5, 2),
    )
    
    max_storage_temp = fields.Float(
        string='Max Storage Temperature (°C)',
        help='Maximum temperature at which the product can be safely stored',
        tracking=True,
        digits=(5, 2),
    )
    
    # Temperature conversions (computed fields)
    min_operating_temp_f = fields.Float(
        string='Min Operating Temperature (°F)',
        compute='_compute_fahrenheit_temps',
        inverse='_inverse_min_operating_temp_f',
        readonly=True,
        tracking=True,
        digits=(5, 2),
        help='Minimum operating temperature in Fahrenheit',
    )
    
    max_operating_temp_f = fields.Float(
        string='Max Operating Temperature (°F)',
        compute='_compute_fahrenheit_temps',
        inverse='_inverse_max_operating_temp_f',
        readonly=True,
        tracking=True,
        digits=(5, 2),
        help='Maximum operating temperature in Fahrenheit',
    )
    
    min_storage_temp_f = fields.Float(
        string='Min Storage Temperature (°F)',
        compute='_compute_fahrenheit_temps',
        inverse='_inverse_min_storage_temp_f',
        readonly=True,
        tracking=True,
        digits=(5, 2),
        help='Minimum storage temperature in Fahrenheit',
    )
    
    max_storage_temp_f = fields.Float(
        string='Max Storage Temperature (°F)',
        compute='_compute_fahrenheit_temps',
        inverse='_inverse_max_storage_temp_f',
        readonly=True,
        tracking=True,
        digits=(5, 2),
        help='Maximum storage temperature in Fahrenheit',
    )
    
    temp_range_visualization = fields.Char(
        string='Temperature Range', 
        compute='_compute_temp_range_visualization',
        help='Visual representation of the temperature range for list views',
    )
    
    # Humidity specifications
    min_operating_humidity = fields.Float(
        string='Min Operating Humidity (%)',
        help='Minimum humidity level at which the product can safely operate',
        tracking=True,
        digits=(5, 2),
    )
    
    max_operating_humidity = fields.Float(
        string='Max Operating Humidity (%)',
        help='Maximum humidity level at which the product can safely operate',
        tracking=True,
        digits=(5, 2),
    )
    
    humidity_range_visualization = fields.Char(
        string='Humidity Range', 
        compute='_compute_humidity_range_visualization',
        help='Visual representation of the humidity range for list views',
    )
    
    # Altitude specifications
    min_operating_altitude = fields.Integer(
        string='Min Operating Altitude (m)',
        help='Minimum altitude at which the product can safely operate',
        tracking=True,
    )
    
    max_operating_altitude = fields.Integer(
        string='Max Operating Altitude (m)',
        help='Maximum altitude at which the product can safely operate',
        tracking=True,
    )
    
    # Altitude conversions (computed fields)
    min_operating_altitude_ft = fields.Integer(
        string='Min Operating Altitude (ft)',
        compute='_compute_feet_altitude',
        inverse='_inverse_min_operating_altitude_ft',
        readonly=True,
        tracking=True,
        help='Minimum operating altitude in feet',
    )
    
    max_operating_altitude_ft = fields.Integer(
        string='Max Operating Altitude (ft)',
        compute='_compute_feet_altitude',
        inverse='_inverse_max_operating_altitude_ft',
        readonly=True,
        tracking=True,
        help='Maximum operating altitude in feet',
    )
    
    # Protection ratings
    ip_rating_id = fields.Many2one(
        'protection.rating',
        string='IP Rating',
        domain=[('rating_type', '=', 'ip')],
        tracking=True,
        help='Ingress Protection rating against dust and water',
    )
    
    ik_rating_id = fields.Many2one(
        'protection.rating',
        string='IK Rating',
        domain=[('rating_type', '=', 'ik')],
        tracking=True,  
        help='Impact protection rating',
    )
    
    # Environmental resistance specifications
    is_vibration_resistant = fields.Boolean(
        string='Vibration Resistant',
        tracking=True,
        help='Product can operate in environments with significant vibrations',
    )
    
    vibration_rating = fields.Char(
        string='Vibration Rating',
        tracking=True,
        help='Vibration resistance specification (e.g., MIL-STD-810G)',
    )
    
    is_uv_resistant = fields.Boolean(
        string='UV Resistant',
        tracking=True,
        help='Product has UV resistance for outdoor applications',
    )
    
    uv_resistance_years = fields.Float(
        string='UV Resistance (years)',
        help='Estimated years of UV resistance before degradation',
        tracking=True,
        digits=(4, 1),
    )
    
    is_salt_spray_resistant = fields.Boolean(
        string='Salt Spray Resistant',
        tracking=True,
        help='Product can resist corrosion from salt spray',
    )
    
    salt_spray_hours = fields.Integer(
        string='Salt Spray Test (hours)',
        tracking=True,
        help='Hours of salt spray resistance in testing',
    )
    
    is_chemical_resistant = fields.Boolean(
        string='Chemical Resistant',
        tracking=True,
        help='Product has resistance to chemical substances',
    )
    
    chemical_resistance_notes = fields.Text(
        string='Chemical Resistance Notes',
        tracking=True,
        help='Details of chemicals the product is resistant to',
    )
    
    is_shock_resistant = fields.Boolean(
        string='Shock Resistant',
        tracking=True,
        help='Product can withstand mechanical shocks',
    )
    
    shock_rating = fields.Char(
        string='Shock Rating',
        tracking=True,
        help='Shock resistance specification (e.g., survive drops from 1.5m)',
    )
    
    # General environmental conditions
    environmental_certifications = fields.Text(
        string='Environmental Certifications',
        help='List of environmental testing certifications obtained',
    )
    
    special_environmental_notes = fields.Text(
        string='Special Environmental Notes',
        help='Additional notes about environmental conditions',
    )
    
    @api.constrains('min_operating_temp', 'max_operating_temp')
    def _check_operating_temp_range(self):
        for record in self:
            if record.min_operating_temp and record.max_operating_temp:
                if record.min_operating_temp > record.max_operating_temp:
                    raise ValidationError(_('Minimum operating temperature cannot be greater than maximum operating temperature.'))
    
    @api.constrains('min_storage_temp', 'max_storage_temp')
    def _check_storage_temp_range(self):
        for record in self:
            if record.min_storage_temp and record.max_storage_temp:
                if record.min_storage_temp > record.max_storage_temp:
                    raise ValidationError(_('Minimum storage temperature cannot be greater than maximum storage temperature.'))
    
    @api.constrains('min_operating_humidity', 'max_operating_humidity')
    def _check_humidity_range(self):
        for record in self:
            if record.min_operating_humidity and record.max_operating_humidity:
                if record.min_operating_humidity > record.max_operating_humidity:
                    raise ValidationError(_('Minimum operating humidity cannot be greater than maximum operating humidity.'))
                if record.min_operating_humidity < 0 or record.max_operating_humidity > 100:
                    raise ValidationError(_('Humidity values must be between 0 and 100 percent.'))
    
    @api.constrains('min_operating_altitude', 'max_operating_altitude')
    def _check_altitude_range(self):
        for record in self:
            if record.min_operating_altitude and record.max_operating_altitude:
                if record.min_operating_altitude > record.max_operating_altitude:
                    raise ValidationError(_('Minimum operating altitude cannot be greater than maximum operating altitude.'))
    
    @api.depends('min_operating_temp', 'max_operating_temp', 
                 'min_storage_temp', 'max_storage_temp')
    def _compute_fahrenheit_temps(self):
        """Convert Celsius to Fahrenheit temperatures"""
        for product in self:
            # Fahrenheit = (Celsius * 9/5) + 32
            if product.min_operating_temp:
                product.min_operating_temp_f = (product.min_operating_temp * 9/5) + 32
            else:
                product.min_operating_temp_f = False
                
            if product.max_operating_temp:
                product.max_operating_temp_f = (product.max_operating_temp * 9/5) + 32
            else:
                product.max_operating_temp_f = False
                
            if product.min_storage_temp:
                product.min_storage_temp_f = (product.min_storage_temp * 9/5) + 32
            else:
                product.min_storage_temp_f = False
                
            if product.max_storage_temp:
                product.max_storage_temp_f = (product.max_storage_temp * 9/5) + 32
            else:
                product.max_storage_temp_f = False
    
    def _inverse_min_operating_temp_f(self):
        """Convert Fahrenheit to Celsius for min_operating_temp"""
        for product in self:
            if product.min_operating_temp_f:
                product.min_operating_temp = (product.min_operating_temp_f - 32) * 5/9
            else:
                product.min_operating_temp = False
    
    def _inverse_max_operating_temp_f(self):
        """Convert Fahrenheit to Celsius for max_operating_temp"""
        for product in self:
            if product.max_operating_temp_f:
                product.max_operating_temp = (product.max_operating_temp_f - 32) * 5/9
            else:
                product.max_operating_temp = False
    
    def _inverse_min_storage_temp_f(self):
        """Convert Fahrenheit to Celsius for min_storage_temp"""
        for product in self:
            if product.min_storage_temp_f:
                product.min_storage_temp = (product.min_storage_temp_f - 32) * 5/9
            else:
                product.min_storage_temp = False
    
    def _inverse_max_storage_temp_f(self):
        """Convert Fahrenheit to Celsius for max_storage_temp"""
        for product in self:
            if product.max_storage_temp_f:
                product.max_storage_temp = (product.max_storage_temp_f - 32) * 5/9
            else:
                product.max_storage_temp = False
    
    @api.depends('min_operating_altitude', 'max_operating_altitude')
    def _compute_feet_altitude(self):
        """Convert meters to feet for altitude values"""
        for product in self:
            # 1 meter = 3.28084 feet
            if product.min_operating_altitude:
                product.min_operating_altitude_ft = int(product.min_operating_altitude * 3.28084)
            else:
                product.min_operating_altitude_ft = False
                
            if product.max_operating_altitude:
                product.max_operating_altitude_ft = int(product.max_operating_altitude * 3.28084)
            else:
                product.max_operating_altitude_ft = False
    
    def _inverse_min_operating_altitude_ft(self):
        """Convert feet to meters for min_operating_altitude"""
        for product in self:
            if product.min_operating_altitude_ft:
                product.min_operating_altitude = int(product.min_operating_altitude_ft / 3.28084)
            else:
                product.min_operating_altitude = False
    
    def _inverse_max_operating_altitude_ft(self):
        """Convert feet to meters for max_operating_altitude"""
        for product in self:
            if product.max_operating_altitude_ft:
                product.max_operating_altitude = int(product.max_operating_altitude_ft / 3.28084)
            else:
                product.max_operating_altitude = False
    
    @api.depends('min_operating_temp', 'max_operating_temp')
    def _compute_temp_range_visualization(self):
        """Create a textual representation of temperature range for list views"""
        for product in self:
            if product.min_operating_temp and product.max_operating_temp:
                product.temp_range_visualization = f"{product.min_operating_temp}°C to {product.max_operating_temp}°C"
            elif product.min_operating_temp:
                product.temp_range_visualization = f"≥ {product.min_operating_temp}°C"
            elif product.max_operating_temp:
                product.temp_range_visualization = f"≤ {product.max_operating_temp}°C"
            else:
                product.temp_range_visualization = False
    
    @api.depends('min_operating_humidity', 'max_operating_humidity')
    def _compute_humidity_range_visualization(self):
        """Create a textual representation of humidity range for list views"""
        for product in self:
            if product.min_operating_humidity and product.max_operating_humidity:
                product.humidity_range_visualization = f"{product.min_operating_humidity}% to {product.max_operating_humidity}%"
            elif product.min_operating_humidity:
                product.humidity_range_visualization = f"≥ {product.min_operating_humidity}%"
            elif product.max_operating_humidity:
                product.humidity_range_visualization = f"≤ {product.max_operating_humidity}%"
            else:
                product.humidity_range_visualization = False
