# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.addons.base_geoengine import geo_model
from odoo.addons.base_geoengine import fields as geo_fields

from datetime import timedelta, date
import json
import logging

_logger = logging.getLogger(__name__)

class municipality(models.Model):
    _name = 'bedit_ecoles.municipality'
    _order = 'name asc'
    _description = 'Municipality'

    name = fields.Char(string='Municipality',required=True)

class postcode(models.Model):
    _name = 'bedit_ecoles.postcode'
    _order = 'name asc'
    _description = 'Postcode'

    name = fields.Char(string='Postcode', size=4, required=True)

class school_type(models.Model):
    _name = 'bedit_ecoles.school_type'
    _order = 'name asc'
    _description = 'SchoolType'

    name = fields.Char(string='Type', size=3, required=True)
    description  = fields.Char(string='Description', size=50)

class company(geo_model.GeoModel):
    _name = 'bedit_ecoles.company'
    _order = 'name asc'
    _description = 'Company'

    name = fields.Char(string='Name',required=True)
    address = fields.Char(string='Address', required=False)
    polnum = fields.Char(string='Polnum', required=False)

    the_geom =  geo_fields.GeoPoint(required=True, srid=31370, gist_index=True)

    postcode_id = fields.Many2one('bedit_ecoles.postcode', string="Postcode")
    municipality_id = fields.Many2one('bedit_ecoles.municipality', string="Municipality")

class school(geo_model.GeoModel):
    _name = 'bedit_ecoles.school'
    _order = 'name asc'
    _description = 'School'

    name = fields.Char(string='Name',required=True)
    address = fields.Char(string='Address', required=False)
    polnum = fields.Char(string='Polnum', required=False)

    the_geom =  geo_fields.GeoPoint(required=True, srid=31370, gist_index=True)

    postcode_id = fields.Many2one('bedit_ecoles.postcode', string="Postcode")
    municipality_id = fields.Many2one('bedit_ecoles.municipality', string="Municipality")
    stype_id = fields.Many2one('bedit_ecoles.school_type', string="School type")

class activity(geo_model.GeoModel):
    _name = 'bedit_ecoles.activity'
    _order = 'name asc'
    _description = 'Activity'

    description = fields.Char(string='Description', size=50)

    @api.model
    def _year_between(self):
        years = []
        year_min = 2010
        year_max = (date.today().year)+1
        for x in range(year_min, year_max):
            years.append((str(x),str(x)))
        return years

    def _get_this_year(self):
        return str(date.today().year)

    year = fields.Selection('_year_between', string="Year", default=lambda self: self._get_this_year(), required=True)#TODO add min/max val
    school_id = fields.Many2one('bedit_ecoles.school', string="School", required=True)
    company_id = fields.Many2one('bedit_ecoles.company', string="Company", required=True)
    number = fields.Integer(string = 'Number of participant')

    @api.depends('school_id', 'company_id', 'year')
    def _get_name(self):
        for record in self:
            name = ''
            if (record.year and record.school_id and record.company_id):
                name = '%s / %s (%s)' % (record.school_id.name, record.company_id.name, record.year)
            record.name = name

    name = fields.Char(compute='_get_name')

    school_muni = fields.Char(related='school_id.municipality_id.name', store=False)
    company_muni = fields.Char(related='company_id.municipality_id.name', store=False)

    school_type = fields.Char(related='school_id.stype_id.name', store=False)

    the_geom = geo_fields.GeoPoint(related='school_id.the_geom', store=False)
