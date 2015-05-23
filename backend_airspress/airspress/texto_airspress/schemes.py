'''
All the logic that backs the airspress messaging.
'''
from firebase_token_generator import create_token
from firebase import Firebase
from account.actions import get_profile_pic
from signup.schemes import User
from parse_rest.query import QueryResourceDoesNotExist
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
    channel = "deals"
    node = "data/airdeals/"
    users ="dealers"
    if source=="direct_messaging":
        node = "data/directMessaging/"
        channel = "conversations"
        users = "members"
        
    reference = auth_server(node)
    
    channel_ref = reference.child(channel)
    users_ref = reference.child(users)
    
    
    # add members to conversation node
    channel_dic = {}
    members = {}
    for user_id in members_list:
        members[user_id]=True
    try:    
        this_channel = channel_ref.child(channel_id)
        this_channel.update({'members':members})
    except:
        channel_dic[channel_id]={'members':members}
        channel_ref.update(channel_dic)
    # add conversation to messages node
    
    users_dic = {}
    members = {}
    for user_id in members_list:
        try:
            user_channel_ref = users_ref.child(user_id + "/" + channel)
            user_channel_ref.update({channel_id:True})
        except:
            users_dic[user_id]={channel:{channel_id:True}}
            users_ref.update(users_dic)
       
    return node+'messages'
            
def retrieve_conversation(user_id):
    node = "data/directMessaging/members/"+user_id+"/conversations/"
    reference = auth_server(node)
    inbox = reference.get()
    print inbox
    convos={}
    i = 0
    try:
        for k,v in inbox.items():
            i+=1
            node = "data/directMessaging/conversations/"+k
            reference = auth_server(node)
            inside = reference.get()
            inside_inbox = inside.get('inbox',{})
            inside_members = inside.get('members',{})
            
                    
            senderId = inside_inbox.get('senderId',False)
            senderName = inside_inbox.get('senderName',False)
            text = inside_inbox.get('text', False)
            pub_date = inside_inbox.get('pub_date', False)
            pPicture = get_profile_pic(senderId)
            if senderId:
                convos['conv'+str(i)]={'senderId':senderId,'senderName':senderName,
                              'text':text,'pub_date':pub_date,'pPicture':pPicture, 'source_id':k}
                for m,b in inside_members.items():
                    if not (m == user_id):
                        print 'magueule'
                        try:
                            convos['conv'+str(i)]['other_name'] = User.Query.get(objectId=m).username
                        except (AttributeError, QueryResourceDoesNotExist):
                            pass
    except:
        pass                    
    return convos