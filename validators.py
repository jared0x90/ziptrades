#!/usr/bin/env pypy

def valid_zipcode(zipcode):
    return len(zipcode) == 5 and zipcode.isdigit() 