 
from signup.schemes import User

# Some users might lack profile pic
# i don't want to be overwhelmed by a ton of "try..except" and what-not... 
def get_profile_pic(user_objectid):
    try:
        any_user=User.Query.get(objectId=user_objectid)
        any_user_pic = any_user.profilePicture.url
    except:
        void = ''
        return void
    return any_user_pic

def get_notifications(user_objectid):
    target_user = User.Query.get(objectId = user_objectid)
    notif_inbox = getattr(target_user,'notifInbox', '')
    notif_out_deals = getattr(target_user,'notifOutDeals','')
    notif_in_deals = getattr(target_user, 'notifInDeals', '')
    total = sum([i for i in [notif_in_deals,notif_inbox,notif_out_deals] if i])
    notif_dict = {'inbox':notif_inbox,'out_deals':notif_out_deals,'in_deals':notif_in_deals,'total':total}
    
    return notif_dict