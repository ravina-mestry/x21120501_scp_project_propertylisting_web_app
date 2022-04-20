# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Property    # Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('listing_type','property_type','ber_rating','county','price','agent_email')

admin.site.register(Property,PropertyAdmin)

