import requests
import re

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

url = 'http://www.cante.com.br/baixar.php?id='
num = '26'

for num in range(23,8992,1):
    try:
        r = requests.get(url+str(num), allow_redirects=True)
        filename = get_filename_from_cd(str(r.headers.get('content-disposition')))
        if filename is None:
            filename = url+ str(num)
        else:
            filename = filename.replace('"', '')
            open(filename,'wb').write(r.content)
    except: 
        open("erros.txt", 'w').write(filename)
        print (str(num) + filename + "Arquivo com erro")
        pass
