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
def create_conversation(channel_id, members_list, source=None):
    channel = ""
    node = ""
    users = ""
    if source=="direct_messaging":
        node = "data/directMessaging/"
        channel = "conversations"
        users = "users"
        
    reference = auth_server(node if node else "data/airdeals/")
    channel_ref = reference.child(channel if channel else "deals")
    users_ref = reference.child(users if users else "dealers")
    
    
    # update with deal info
    channel_dic = {}
    members = {}
    for user_id in members_list:
        members[user_id]=True
        
    channel_dic[channel_id]={'members':members}
    channel_ref.update(channel_dic)
    
    # update with dealers info
    
    users_dic = {}
    members = {}
    for user_id in members_list:
        try:
            user_channel_ref = users_ref.child(user_id + "/" + (channel if channel else "deals"))
            user_channel_ref.update({channel_id:True})
        except:
            users_dic[user_id]={(channel if channel else 'deals'):{channel_id:True}}
            users_ref.update(users_dic)
    return node+'messages'
            
def retrieve_conversation():
    reference = auth_server("data/airdeals/")
    message_ref = reference.child("messages")
    return