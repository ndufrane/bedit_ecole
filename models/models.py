# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.addons.base_geoengine import geo_model
from odoo.addons.base_geoengine import fields as geo_fields

from datetime import timedelta
import json
import logging

_logger = logging.getLogger(__name__)

class municipality(models.Model):
    _name = 'bedit_ecole.municipality'
    _order = 'name asc'
    _description = 'Municipality'

    name = fields.Char(string='Municipality',required=True)

class postcode(models.Model):
    _name = 'bedit_ecole.postcode'
    _order = 'name asc'
    _description = 'Postcode'

    name = fields.Char(string='Postcode', size=4, required=True)

class school_type(models.Model):
    _name = 'bedit_ecole.school_type'
    _order = 'name asc'
    _description = 'SchoolType'

    name = fields.Char(string='Type', size=3, required=True)
    description  = fields.Char(string='Description', size=50)

class company(geo_model.GeoModel):
    _name = 'bedit_ecole.company'
    _order = 'name asc'
    _description = 'Company'

    name = fields.Char(string='Name',required=False)
    address = fields.Char(string='Address', required=False)
    polnum = fields.Char(string='Polnum', required=False)

    the_geom =  geo_fields.GeoPoint(required=True, srid=31370, gist_index=True)

    postcode_id = fields.Many2one('bedit_ecole.postcode', string="Postcode")
    municipality_id = fields.Many2one('bedit_ecole.municipality', string="Municipality")

class school(geo_model.GeoModel):
    _name = 'bedit_ecole.school'
    _order = 'name asc'
    _description = 'School'

    name = fields.Char(string='Name',required=False)
    address = fields.Char(string='Address', required=False)
    polnum = fields.Char(string='Polnum', required=False)

    the_geom =  geo_fields.GeoPoint(required=True, srid=31370, gist_index=True)

    postcode_id = fields.Many2one('bedit_ecole.postcode', string="Postcode")
    municipality_id = fields.Many2one('bedit_ecole.municipality', string="Municipality")
    stype_id = fields.Many2one('bedit_ecole.school_type', string="School type")

class activity(models.Model):
    _name = 'bedit_ecole.activity'
    _order = 'name asc'
    _description = 'Activity'

    description = fields.Char(string='Description', size=50)
    year = fields.Integer(string="Year")#TODO add min/max val
    school = fields.Many2one('bedit_ecole.school', string="School")
    company = fields.Many2one('bedit_ecole.company', string="Company")
    number = fields.Integer(string = 'number of participant')
