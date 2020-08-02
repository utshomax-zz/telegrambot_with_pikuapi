#imports
from bot import telegram_chatbot
from commands import command
import sqlite3
from time import sleep

#veriables
bot = telegram_chatbot("config.cfg")
cmd= command('config.cfg')
user_id=None
user_name=None
update_id = None
user_username=None
#dbloading with any quiry
def loaddb(quiry,pram):
   
    try:
        conn = sqlite3.connect('db_pikupyhton.db')#pylint: disable=E1101
        cursor = conn.cursor()
        count= conn.execute(quiry,pram)
        num=count.fetchone()
        conn.commit()
        cursor.close()
        return num
        

    except sqlite3.Error as error:#pylint: disable=E1101
        #send a notifiacation to me!
        print("db error!",error)
    finally:
        if (conn):
            conn.close()

#sending repaly
def make_reply(msg):
    reply = None
    if msg is not None:
        if check_user(user_id) is True:
            if msg=='/start':
                reply='sending a keybord'
           
           #return a kryboard also
            else:
               reply = 'Hey {}! How can I help you?'.format(user_name)
       

        elif msg=='/register':
            if check_user(user_id) is False:
                reply="Enter your roll No with a 'r' at first. Example:r123456"
            else:
                reply='You are already registered ! If you want to change your Roll no,please command /changeroll'
        elif msg[0]=='r' or msg[0]=='R':
            if check_user(user_id) is False:
                user_roll=str(msg[1:])
                barnch=str(msg[4:6])
                try:
                    user_reg(user_id,user_name,user_username,user_roll,barnch)
                except:
                    reply="Sorry! Something went wrong! Please feel free to report a bug by typing /reportbug"    
           
        else:
            print(msg)
            res=cmd.getReply(msg)
            try:
                reply=res['reply']
            except:
                reply="Sorry! Something went wrong! Please feel free to report a bug by typing /reportbug"
            print(reply)
           # reply='Hey {}! You are not registered yet. Please register by command /register'.format(user_name)
    return reply


#commands to exicute




#checking user exist or not
def check_user(userid):
    user_exist='''SELECT count(*) FROM users WHERE user_id=?'''
    p=(userid,)
    a=loaddb(user_exist,p)
    if a[0]>=1:
       
        return True
    else:
        
        return False

    

#registering user if not registered
def user_reg(u_id,u_name,u_username,u_roll,u_branch):
    q='''INSERT INTO users (user_id ,name ,roll ,username ,branch) VALUES(?,?,?,?,?)'''
    p=( u_id ,u_name ,u_username ,u_roll ,u_branch)
    loaddb(q,p)










#updater for listioning continuously to user
while True:
    updates=None
    try:
        updates = bot.get_updates(offset=update_id)
        if updates!=None:
            updates = updates["result"]
        else:
            errorthrowingfunction("haha")
    except:
        sleep(30)
        bot.send_message("Server isuue. It will be fixed soon", 988155186)

    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            user_id = int(item["message"]["from"]["id"])
            user_name= str(item["message"]["from"]["first_name"])
            user_username=str(item["message"]["from"]["username"])
            reply = make_reply(message)
            bot.send_message(reply, user_id)