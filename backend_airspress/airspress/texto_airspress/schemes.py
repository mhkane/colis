'''
All the logic that backs the airspress messaging.
'''
from firebase_token_generator import create_token
from firebase import Firebase
FIREBASE_SECRET = "71HVpGHakz0lUGWJlMvGzM9MPTEcRBHSGTnh1A1q"
ROOT_URL_FIREBASE = "https://radiant-torch-2520.firebaseio.com/"
def auth_client(user_id, source, source_id):
    auth_payload = {"uid": "custom:"+user_id, "user_id": user_id, "source": source, 'source_id':source_id}
    token = create_token(FIREBASE_SECRET, auth_payload)
    return token

def auth_server(node):
    auth_payload = {"uid": "custom:1", "user_id":"master"}
    token = create_token(FIREBASE_SECRET, auth_payload)
    f = Firebase(ROOT_URL_FIREBASE+node, auth_token=token)
    return f
# create conversation channel for a deal
def create_conversation(deal_id, members_list):
    reference = auth_server("data/airdeals/")
    deals_ref = reference.child("deals")
    dealers_ref = reference.child("dealers")
    
    
    # update with deal info
    deals_dic = {}
    members = {}
    for user_id in members_list:
        members[user_id]=True
        
    deals_dic[deal_id]={'members':members}
    deals_ref.update(deals_dic)
    
    # update with dealers info
    
    dealers_dic = {}
    members = {}
    for user_id in members_list:
        try:
            user_deal_ref = dealers_ref.child(user_id+"/deals")
            user_deal_ref.update({deal_id:True})
        except:
            dealers_dic[user_id]={'deals':{deal_id:True}}
            dealers_ref.update(dealers_dic)
    return True
            
def retrieve_conversation():
    reference = auth_server("data/airdeals/")
    message_ref = reference.child("messages")
    return