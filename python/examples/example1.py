#!/usr/bin/env python
#
# Copyright 2011 MERS Technologies.
#

from subuno import SUBUNOAPI

result = SUBUNOAPI().run(
	apikey = "2g4g747g843",
	data = {
		"t_id"            : "7d3n89wn" ,
		"ip_addr"         : "24.24.24.24",
		"customer_name"   : "John Doe",
		"phone"           : "212-456-7890",
		"email"           : "john.doe@domain.com",
		"company"         : "Doe LLC",
		"price"           : "50.0",
		"shipping_method" : "day1",
		"bin"             : "480128",

		"bill_street1"    : "12 East 71th St",
		"bill_street2"    : "#12",
		"bill_city"       : "New York",
		"bill_state"      : "NY",
		"bill_country"    : "US" ,
		"bill_zip"        : "10021",

		"ship_street1"    : "12 East 71th St",
		"ship_street2"    : "#12",
		"ship_city"       : "New York",
		"ship_state"      : "NY",
		"ship_country"    : "US",
		"ship_zip"        : "10021",
	},
)

#result is a python dictionary with keys/value pairs with data returned by api.
print result["action"]
print result["ref_code"]