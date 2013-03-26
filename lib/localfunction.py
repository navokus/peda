#
# PEDA - Python Exploit Development Assistance for GDB
#
# Copyright (C) 2012 - Navokus 
#
# License: see LICENSE file for details
#

class ContextCode(object):
    """
    Class to access global options of PEDA commands and functions
    TODO: save/load option to/from file
    """
    codes = {}
    def __init__(self):
        """option format: name = (value, comment) """
        pass


    @staticmethod
    def reset():
        """clear renamed functions"""
        ContextCode.codes.clear()
        return True

    @staticmethod
    def show(name=""):
        """display renamed functions in binary"""
        result = {}
        for opt in ContextCode.codes.keys():
			result[opt] = ContextCode.codes[opt]
         
        return result

    @staticmethod
    def get_value(name):
        """get function"""
        if name in ContextCode.codes.keys():
            return ContextCode.codes[name][0]
        else:
            return None

    @staticmethod
    def set(name, value):
        """set option"""
        ContextCode.codes[name] = (value,"")
        return True
    
    @staticmethod
    def add_comment(name, comment):
        """add command """
        if name in ContextCode.codes.keys():
            value = ContextCode.codes[name][0]
            ContextCode.codes[name] = (value,comment)
            return True
        else:
            return None
    
    @staticmethod
    def find_key(val):
		"""return the key of dictionary dic given the value"""
		result = [k for k, v in ContextCode.codes.iteritems() if v[0] == val]
		if not result:
			return None
		else:
			return result[0]

    @staticmethod
    def help(name=""):
        """display help info of rename function"""
        result = {}
        for f in ContextCode.codes:
            if name in f and not f.startswith("_"):
                result[f] = ContextCode.codes[f][1]
        return result
        
    @staticmethod
    def write(filename):
        """write local function renamed to file"""
        result = {}
        for opt in ContextCode.codes.keys():
			result[opt] = ContextCode.codes[opt]
         
        return result

