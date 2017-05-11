from includes.ActiveCampaign import ActiveCampaign
from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
import datetime

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
    message = {
        'format': 'mime',
        'subject': 'This is a Great Email!',
        'fromemail': 'anneknies@me.com',
        'fromname': 'Anne Nies',
        'reply2': 'noreply@example.com',
        'priority': 3,
        'charset': 'utf-8',
        'encoding': 'quoted-printable',
        'htmlconstructor': 'external',
        'htmlfetch': 'http://tplshare.com/Il7bx80',
        'htmlfetchwhen': 'send',
        'textconstructor': 'external',
        'textgetch': 'http://tplshare.com/Il7bx80',
        'textfetchwhen': 'send',
        'p[1]': 1
     }
    print(ac.api('message/add', message))