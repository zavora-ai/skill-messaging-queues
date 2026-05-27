#!/usr/bin/env python3
"""Queue health check."""
import json,sys
def check(data):
    depth=data.get("depth",0);rate=data.get("rate",1)
    growing=depth>100 and rate<depth/10
    return {"healthy":not growing,"depth":depth,"rate":rate,"alert":"Queue growing — scale consumers" if growing else "OK"}
if __name__=="__main__":print(json.dumps(check(json.loads(sys.argv[1])),indent=2))
