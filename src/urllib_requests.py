import urllib.request

def urllib_request():

    my_url = urllib.request.urlopen('https://www.nytimes.com/')
    print(my_url.geturl())

    '''https: // www.nytimes.com /'''

    print(my_url.info())
    '''
    Connection: close
    Content - Length: 2231610
    Server: nginx
    Content - Type: text / html;
    charset = utf - 8
    x - b3 - traceid: d4f288a7c4ab45de8bfd79895fd94167
    x - nyt - data - last - modified: Fri, 04
    Mar
    2022
    17: 31:39
    GMT
    Last - Modified: Fri, 04
    Mar
    2022
    17: 31:39
    GMT
    X - PageType: vi - homepage
    X - XSS - Protection: 1;
    mode = block
    X - Content - Type - Options: nosniff
    cache - control: s - maxage = 30, no - cache
    x - nyt - route: homepage
    X - Origin - Time: 2022 - 03 - 04
    17: 31:55
    UTC
    Accept - Ranges: bytes
    Date: Fri, 04
    Mar
    2022
    17: 31:55
    GMT
    Age: 0
    X - Served - By: cache - lga21929 - LGA, cache - fty21333 - FTY
    X - Cache: MISS, MISS
    X - Cache - Hits: 0, 0
    X - Timer: S1646415113
    .332570, VS0, VE1936
    Vary: Accept - Encoding, Fastly - SSL
    Set - Cookie: nyt - a = ed4gGJZ0gSypR8V6ernv4l;
    Expires = Sat, 04
    Mar
    2023
    17: 31:55
    GMT;
    Path = /; Domain =.nytimes.com;
    SameSite = none;
    Secure
    x - nyt - app - webview: 0
    Set - Cookie: nyt - gdpr = 0;
    Expires = Fri, 04
    Mar
    2022
    23: 31:55
    GMT;
    Path = /; Domain =.nytimes.com
    x - gdpr: 0
    Set - Cookie: nyt - purr = cfhhcfhhhckf;
    Expires = Sat, 04
    Mar
    2023
    17: 31:55
    GMT;
    Path = /; Domain =.nytimes.com;
    SameSite = Lax;
    Secure
    Set - Cookie: nyt - geo = US;
    Expires = Fri, 04
    Mar
    2022
    23: 31:55
    GMT;
    Path = /; Domain =.nytimes.com
    X - Frame - Options: DENY
    onion - location: https: // www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion /
    X - API - Version: F - F - VI
    Content - Security - Policy: upgrade - insecure - requests;
    default - src
    data: 'unsafe-inline' 'unsafe-eval'
    https:;
    script - src
    data: 'unsafe-inline' 'unsafe-eval'
    https: blob:; style - src
    data: 'unsafe-inline'
    https:;
    img - src
    data: https: blob:;
    font - src
    data: https:; connect - src
    https: wss: blob:;
    media - src
    data: https: blob:;
    object - src
    https:;
    child - src
    https: data: blob:;
    form - action
    https:;
    report - uri
    https: // csp.nytimes.com / report;
    Strict - Transport - Security: max - age = 63072000;
    preload;
    includeSubdomains
    Set - Cookie: nyt - b3 - traceid = d4f288a7c4ab45de8bfd79895fd94167;
    Path = /; Domain =.nytimes.com;
    SameSite = none;
    Secure
    x - nyt - edge - cache: MISS - MISS'''
    
    print(my_url.getcode())

    '''200'''




