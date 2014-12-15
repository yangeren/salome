__author__ = 'yer'
#*--coding=utf-8--*
import dns.resolver
import httplib
import os

iplist = []
appdomain = 'www.google.com'

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
        CNAME = dns.resolver.query(domain, 'cname')
    except Exception,e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        print i
        for j in i.items:
            print j.address
            iplist.append(j.address)
    for m in CNAME.response.answer:
        print m
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers = {"Host": appdomain})

        r = conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent == "<!doctype html>":
            print(ip+"  [OK]")
        else:
            print(ip + "  [Error]")


if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)

        else:
            print "dns resolver error"
