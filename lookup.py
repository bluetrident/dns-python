import dns.resolver

dname = raw_input('Enter domain name for lookup: ')

answers = dns.resolver.query(dname, 'A')
for rdata in answers:
    print rdata.address


