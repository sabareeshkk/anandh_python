# Program to implement JSON record

def json_encode(data):
	if isinstance(data, bool):
        	if data:
        		return "true"
        	else:
        		return "false"
	elif isinstance(data, (int, float)):
    		return str(data)
	elif isinstance(data, str):
        	return '"' + escape_string(data) + '"'
	elif isinstance(data, list):
        	return "[" + ", ".join(json_encode(d) for d in data) + "]"
	elif isinstance(data,dict):
		return "{" + ", ".join(json_encode(d)+':'+json_encode(p) for d,p in data.items())+"}"
	else:
        	raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
	s = s.replace('"', '\\"')
	s = s.replace("\t", "\\t")
	s = s.replace("\n", "\\n")
	return s
