from includes.ActiveCampaign import ActiveCampaign
from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
import time, datetime

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## create
    sdate = datetime.datetime.now() + datetime.timedelta(days=5, hours=12, minutes=1)
    campaign = {
        'type': 'single',
        'name': 'Final Test',
        'sdate': time.strftime('%Y-%m-%d %H:%M:%S', sdate.timetuple()),
        'status': 1,
        'public': 1,
        'tracklinks': 'all',
        'trackreads': 1,
        'htmlunsub': 1,
        'p[1]': 1,
        'm[6]': 1
    }


    print ac.api('campaign/create', campaign)

