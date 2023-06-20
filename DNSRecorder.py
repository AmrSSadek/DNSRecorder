import dns.resolver
from optparse import OptionParser

parser = OptionParser("""
                 

                                                                                                                                          
                       ,--.                                                             ,----..                                           
    ,---,            ,--.'|   .--.--.            ,-.----.        ,---,.   ,----..      /   /   \   ,-.----.        ,---,       .--.--.    
  .'  .' `\      ,--,:  : |  /  /    '.          \    /  \     ,'  .' |  /   /   \    /   .     :  \    /  \     .'  .' `\    /  /    '.  
,---.'     \  ,`--.'`|  ' : |  :  /`. /          ;   :    \  ,---.'   | |   :     :  .   /   ;.  \ ;   :    \  ,---.'     \  |  :  /`. /  
|   |  .`\  | |   :  :  | | ;  |  |--`           |   | .\ :  |   |   .' .   |  ;. / .   ;   /  ` ; |   | .\ :  |   |  .`\  | ;  |  |--`   
:   : |  '  | :   |   \ | : |  :  ;_             .   : |: |  :   :  |-, .   ; /--`  ;   |  ; \ ; | .   : |: |  :   : |  '  | |  :  ;_     
|   ' '  ;  : |   : '  '; |  \  \    `.          |   |  \ :  :   |  ;/| ;   | ;     |   :  | ; | ' |   |  \ :  |   ' '  ;  :  \  \    `.  
'   | ;  .  | '   ' ;.    ;   `----.   \         |   : .  /  |   :   .' |   : |     .   |  ' ' ' : |   : .  /  '   | ;  .  |   `----.   \ 
|   | :  |  ' |   | | \   |   __ \  \  |         ;   | |  \  |   |  |-, .   | '___  '   ;  \; /  | ;   | |  \  |   | :  |  '   __ \  \  | 
'   : | /  ;  '   : |  ; .'  /  /`--'  /         |   | ;\  \ '   :  ;/| '   ; : .'|  \   \  ',  /  |   | ;\  \ '   : | /  ;   /  /`--'  / 
|   | '` ,/   |   | '`--'   '--'.     /          :   ' | \.' |   |    \ '   | '/  :   ;   :    /   :   ' | \.' |   | '` ,/   '--'.     /  
;   :  .'     '   : |         `--'---'           :   : :-'   |   :   .' |   :    /     \   \ .'    :   : :-'   ;   :  .'       `--'---'   
|   ,.'       ;   |.'                            |   |.'     |   | ,'    \   \ .'       `---`      |   |.'     |   ,.'                    
'---'         '---'                              `---'       `----'       `---`                    `---'       '---'                      
                                                                                                                                          
                            			@0x3mr                        
                                                    
script.py [option]
--------------------
-d 	     :: Set Your Specific Target.
-t /  --type :: Set Your Specific DNS Record.

EX:
    dnsrecord.py -d domain.com -t A
To Collect all DNS Records:
    dnsrecord.py -d domain.com -t ANY  
""")

parser.add_option("-d", dest = "domain", type = "string", help = "Your Domain")
parser.add_option("-t", "--type", dest = "dnstype", type = "string", help = "type of DNS Record")

(options, args) = parser.parse_args()

if options.domain == None or options.dnstype == None:
    print(parser.usage)
    exit(0)

elif options.domain != None and options.dnstype != None:

	if options.dnstype == "ANY":
		for options.dnstype in 'A' , 'AAAA', 'PTR', 'CNAME', 'SRV', 'NS', 'MX', 'TXT':
			results = dns.resolver.query(options.domain,options.dnstype,raise_on_no_answer=False)
			if results.rrset is not None:
				print(results.rrset)
	else:
		DNStype = str(options.dnstype)
		DNStype = DNStype.split(",")
		for DnsType in DNStype:
			results = dns.resolver.query(options.domain,DnsType,raise_on_no_answer=False)
			if results.rrset is not None:
					print(results.rrset)
