
def minimal_tsp():
    return { "COMMENT"          : ""
           , "DIMENSION"        : None
           , "TYPE"             : None
           , "EDGE_WEIGHT_TYPE" : None
           , "DATA" : []}


def scan_keywords(tsp,tspfile):
    for line in tspfile:
        words   = line.split(":")
        keyword = words[0].strip()

        if keyword == "COMMENT":
            tsp["COMMENT"] += words[1].strip()
        elif keyword == "NAME":
            tsp["NAME"] = words[1].strip()
        elif keyword == "TYPE":
            tsp["TYPE"] = words[1].strip()
        elif keyword == "DIMENSION":
            tsp["DIMENSION"] = int(words[1].strip())
        elif keyword == "EDGE_WEIGHT_TYPE":
            tsp["EDGE_WEIGHT_TYPE"] = words[1].strip()        
        elif keyword == "NODE_COORD_SECTION": 
            pass
        elif keyword == "EOF":
            break
	else:
            words   = line.split()
            if tsp["EDGE_WEIGHT_TYPE"] == "EUC_2D":
               tsp["DATA"].append( [float(words[1]), float(words[2])] )
  

def read_tsp_file(path):
    tspfile = open(path,'r')
    tsp     = minimal_tsp()
    scan_keywords(tsp,tspfile)
    tspfile.close()
    return tsp


