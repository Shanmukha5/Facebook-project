# pre-installed Packages are--- termcolor, getpass, PIL or PILLOW(according to your python version)


ids=[];dict={};
from termcolor import colored

def Login():
  user_name=raw_input(colored("Enter user name: ",'yellow'))
  if(user_name in ids):
    import getpass
    password=getpass.getpass(colored("Enter password(Won't visible): ",'yellow'))
    if(password==dict[user_name]['Password']):
      print colored("You are successfully into your account",'green')
      Fasebook()
    else:
      print colored("Password is incorrect",'red')
  else:
    print colored("User doesn't exist",'red')
    Start()
def Sign_up():
  from termcolor import colored
  print colored("Hoping that you are a new User",'blue')
  sign_loop=0
  while(sign_loop==0):
    global user_name
    user_name=raw_input(colored("Enter user name: ",'yellow'))
    sign_loop1=0
    while(sign_loop1==0):
      if(user_name not in ids):
        import getpass
        pass1=getpass.getpass(colored("Password: ",'yellow'))
        pass2=getpass.getpass(colored("Password again: ",'yellow'))
        if(pass1==pass2):
          dict[user_name]={}
          dict[user_name]['Password']=pass2
          dob_loop=0
          while(dob_loop==0):
            dob=raw_input(colored("Enter Date of Birth(like 08/01/2000): ",'yellow'))
            import re
            if (bool(re.search(r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$',dob))==True): # some bugs are here have solve them
              dict[user_name]['Date of Birth']=dob
              gender_loop=0
              while(gender_loop==0):
                gender_name=raw_input(colored("Your gender[Male(M) or Female(F)]: ",'yellow'))
                if(gender_name=='M' or gender_name=='m' or gender_name=='F' or gender_name=='f'): 
                  if(gender_name=='M' or gender_name=='m'):
                    dict[user_name]['Gender']="Male"
                    gender_name=5
                  elif(gender_name=='F' or gender_name=='f'):
                    dict[user_name]['Gender']='Female'
                    gender_loop=5
                  mail_loop=0    # this has to be in the loop
                  while(mail_loop==0):
                    mail=raw_input(colored("Enter your mail address(make sure that capital look in on off): ",'yellow'))
                    if(bool(re.search(r'\w+@\w+.com',mail))==True): # regular expressions should be more simplified or has to take more mails including university mails and all
                      dict[user_name]['Mail']=mail
                      contact_loop=0
                      while(contact_loop==0):
                        num=raw_input(colored("Enter your Contact number: ",'yellow'))
                        if(bool(re.search(r'[9,8,7,6]\d{9}',num))):
                          dict[user_name]['Contact']=num
                          dict[user_name]['Diary']=[]
                          dict[user_name]["option"]="You haven't entered anything as a notes"
                          dict[user_name]['Friends']=[]
                          dict[user_name]['Accepted_friends']=[]
                          dict[user_name]['Pending_friends']=[]
                          ids.append(user_name)
                          Fasebook()
                          contact_loop=5
                        elif(num==''):
                          dict[user_name]['Contact']='Not given'
                          Fasebook()
                          contact_loop=5
                        else:
                          print colored("It is not a Indian number or It should be of atleast 10 digits",'red')
                        mail_loop=5
                    else:
                      print colored("Incorrect mail address",'red')   
                else:
                  print colored("Incorrect response",'red')
                dob_loop=5
            else:
              print colored("Incorrect pattern. Please Do follow the pattern",'red')
       
            sign_loop=5
            sign_loop1=5
        else:
          print colored("Passwords won't match",'red')
      else:
        print colored("User already exits...",'red')
        sign_loop1=5


def Fasebook():
  from termcolor import colored
  import getpass
  global user_name
  global Fasebook_loop
  Fasebook_loop=0
  while(Fasebook_loop==0):
    print colored("Home(H)\tTimeline(T)\tYour info(I)\tChange info(C)\tHelp(H, not done)\tLog out(Lo)",'blue')  # add HELP tool in this option line
    choice=raw_input(colored("Select any one of those: ",'yellow'))
    if choice=='H' or choice=='h':
      print colored("Home",'yellow')
      Home()
    elif choice=='I' or choice=='i':
      print colored("Your info",'yellow') 
      info()
    elif choice=='C' or choice=='c':####have to complete
      changeinfo_loop=0
      while(changeinfo_loop==0):
        choose=raw_input(colored("Choose which one to edit(Password(P) / Mail(M) / Date of Birth(D) / Contact(C)) : ",'yellow'))  # Have to write edit tools
        passwords_loop=0
        while(passwords_loop==0):
          if(choose=='P' or choose=='p'):
            pas1=getpass.getpass(colored("Enter your current password: ",'yellow'))
            if(pas1==dict[user_name]['Password']):
              pass_new1=getpass.getpass(colored("Enter your new password: ",'yellow'))
              pass_new2=getpass.getpass(colored("Enter again: ",'yellow'))
              if(pass_new1==pass_new2):
                dict[user_name]['Password']=pass_new2
                print colored("Password changed successfully",'yellow')
                passwords_loop=5
                changeinfo_loop=5
              else:
                print colored("Passwords won't match",'red')
            else:
              print colored("Entered password is not matched with the current password of your account",'red')
          elif(choose=='M' or choose=='m'):
            print colored("Mail cannot be changed",'yellow')
            passwords_loop=5
          elif(choose=='D' or choose=='d'):
            dob_loop=0
            while(dob_loop==0):
              import re
              dob=raw_input(colored("Enter the Date of Birth(like 08/01/2000): ",'yellow'))
              if(bool(re.search(r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$',dob))==True): # some bugs are here have solve them
                dict[user_name]['Date of Birth']=dob
                print "Date of Birth has changed"
                dob_loop=5
              else:
                print colored("It doesn't look like the example",'yellow')
          elif(choose=='c' or choose=='C'):
            contact_loop=0
            while(contact_loop==0):
              contact_choice=raw_input(colored("Add another contact(A) or update your contact(U): ",'yellow'))
              if(contact_choice=='A' or contact_choice=='a'):
                new_contact=raw_input(colored("Enter your new contact(this can be done only once later on you have to update your contacts): ",'yellow'))
                if(bool(re.search(r'\d{[10,12]}',new_contact))):
                  dict[user_name]['New_contact']=new_contact
                  contact_loop=5
                else:
                  print colored("Pattern not matched",'yellow')
          else:
            print colored("Incorrect choice",'red') 
    elif(choice=='T' or choice=='t'):
      Timeline()     
    elif(choice=='Lo' or choice=='lo' or choice=='lO' or choice=='LO'):
      print colored("You are logged out\tThank you",'yellow')
      print '~'*100
      Start()
      Fasebook_loop=5
    else:
      print colored("Wrong selection",'red')


def Home():
  home_loop=0
  from PIL import Image
  from termcolor import colored
  import random
  global img_data
  global likes
  global comments     
  while(home_loop==0):
    img_path=random.choice(img_data)
    img=Image.open(img_path)
    img.show()
    global pic_selection
    print colored("like(L)   comment(C)   share(S)   Pic_info(PI)   next pic(N)  back(B) : ",'blue')
    pic_selection=raw_input()
    if(pic_selection=='L' or pic_selection=='l'):
      for i in range(len(img_data)):
        if(img_path==img_data[i]):
          a=likes[img_path]
          b=a+1                  
          likes[img_path]=b 
          break
      likes_loop=0
      while(likes_loop==0):
        more=raw_input(colored("Of the same\tcomment(C)\tshare(S)\tnext pic(N)\tback(B): ",'blue'))
        if(more=='C' or more=='c'):
          comment=raw_input(colored("Enter comment: ",'yellow'))
          for i in range(len(comments)):
            if(img_path==img_data[i]):
              store=' comment: '+comment 
              comments[img_path].append(store)
              break
          likes_loop=5  
        elif(more=='N' or more=='n'):
          likes_loop=5
        elif(more=='B' or more=='b'):
          likes_loop=5
        else:
          print colored("Incorrect response",'red')  
    elif(pic_selection=='C' or pic_selection=='c'):
      comment=raw_input(colored("Enter comment: ",'yellow'))
      for i in range(len(comments)):
        if(img_path==img_data[i]):
          store=' comment: '+comment
          comments[img_path].append(store)
          break
    elif(pic_selection=='S' or pic_selection=='s'):
      global photos_data
      photos_data.append(img_path)
      print colored("You have successfully shared the pic",'yellow')
    elif(pic_selection=='B' or pic_selection=='b'):
      home_loop=5
    elif(pic_selection=='N' or pic_selection=='n'):
      continue
    elif(pic_selection=='pi' or pic_selection=='Pi' or pic_selection=='pI' or pic_selection=='PI'):
      likes_keys=likes.keys()
      for i in range(len(likes_keys)):
        if(img_path==likes_keys[i]):
          print "LIkes: ",likes[img_path]   
          print "Comments",comments[img_path]
      continue
    else:
      print colored("Incorrect reponse",'red')  

def info():
  global user_name
  print colored("User name : ",'yellow'),user_name
  print colored("Date of Birth : ",'yellow'),dict[user_name]['Date of Birth']
  print colored("Your mail : ",'yellow'),dict[user_name]['Mail']
  print colored("Contact number : ",'yellow'),dict[user_name]['Contact']
  print colored("Your password won't be shown",'yellow')
  print colored("Quote (which describes you) ",'yellow'),dict[user_name]['option']
  if(len(dict[user_name]['Friends'])>0):
    print colored("Your friends ",'yellow')
    for i in range(len(dict[user_name]['Friends'])):
      print i
  
first_loop=0
def Start():
 from termcolor import colored
 while(first_loop==0):
  login_choice=raw_input(colored("Login(L)\tSign up(S)",'blue'))
  if(login_choice=='L' or login_choice=='l'):
    Login()
  elif(login_choice=='S' or login_choice=='s'):
    Sign_up()
  else:
    print colored("Something went wrong",'red')

global img_data    
img_data=['']     #The path of the image files should be placed here like in list type
  

global likes
likes={};comments={};photos_data=[]
for i in range(len(img_data)):
  likes[img_data[i]]={}
  likes[img_data[i]]=0
  comments[img_data[i]]={}
  comments[img_data[i]]=[]

def Photos():
  from termcolor import colored
  from PIL import Image
  print colored("Your photos are as follows!!!",'yellow')
  add_choice=raw_input(colored("Do want to add pic(A) or to see your pics(S): ",'yellow'))
  global photos_data
  addphotos_loop=0
  while(addphotos_loop==0):
    if(add_choice=='S' or add_choice=='s'):
      if(len(photos_data)==0):
        print colored("You have no photos added to your account",'yellow')
        addphotos_loop=5
      else:
        len_photos_data=len(photos_data)-1
        for i in range(len_photos_data):
          photo_path=photos_data[len_photos_data]
          img=Image.open(photo_path)
          img.show()
          pic_choice=raw_input(colored("Want to see the next pic[Y/N]: "))
          len_photos_data-=1
          if(pic_choice=='y' or pic_choice=='Y'):
            print "Your next pic is "
            continue
          elif(pic_choice=='n' or pic_choice=='N'):
            break
          else:
            print colored("Incorrect response",'red')
        add_photos=5   
    elif(add_choice=='A' or add_choice=='a'):
      addpic_loop=0
      while(addpic_loop==0):
        global photos_data
        try:
          pic=raw_input(colored("Mention the path of the your pic in this system: ",'yellow'))
          photos_data.append(pic)
          addphotos_loop=5
        except:
          print colored("Path is incorrect",'red')
        else:
          addpic_loop=5
    else:
      print colored("Incorrect selection",'red')
      addphotos_loop=5
         
   
def About():
  print "All we know about you is..."
  info()
  about_choice=raw_input(colored("If you want  anything to add(A) or back(B), wrong input takes you back: ",'yellow'))
  if(about_choice=='a' or about_choice=='A'):
    global user_name
    dict[user_name]['option']=raw_input(colored("Add a quote to your profile:\n\t",'yellow'))
    print colored("It have been saved to your account.",'yellow')


def Timeline():
  from termcolor import colored
  timeline_loop=0
  while(timeline_loop==0):
    timeline_choice=raw_input(colored("About(A)\tFriends(F not done)\tPhotos(P)\tDaily_Dairy(D)\tBack_to_home(B): ",'yellow'))
    if(timeline_choice=='A' or timeline_choice=='a'):
      About()
    elif(timeline_choice=='f' or timeline_choice=='F'):   # Info of friends have to displayed to the user
      for i in ids:
        print i
      friend_choice=raw_input(colored("Want to send friend request(R) or wanna see friend requests you have(S): ",'yellow'))
      if(friend_choice=='R' or friend_choice=='r'):
        friend_request=raw_input(colored("Enter the user_name, whom you send request: ",'yellow'))
        if(friend_request in ids):
          dict[friend_request]['Pending_friends'].append(user_name)
          print colored("Friend request sent",'yellow')   
        else:
          print colored("User name doesn't exist(Please don't ignore case)",'red')
      elif(friend_choice=='s' or friend_choice=='S'):
        print "Your friends are: ",dict[user_name]['Accepted_friends']
        print "You have friend requests from: ",dict[user_name]['Pending_friends']
        friends_choice=raw_input(colored("To delete any friend(D) or Accept friend who is pending(A) or Back(B): ",'yellow'))
        if(friends_choice=='D' or friends_choice=='d'):
          if(len(dict[user_name]['Accepted_friends'])!=0):
            delete_name=raw_input(colored("Enter the user_name of friend you want to delete from your friends list: ",'yellow'))
            if(delete_name in ids):
              delete_choice=raw_input(colored("Do you really want to delete?(Y/N) : ",'yellow'))
              if(delete_choice=='y' or delete_choice=='Y'):
                dict[user_name]['Accepted_friends'].remove(delete_choice)
              elif(delete_choice=='n' or delete_choice=='N'):
                print colored("Deletion process cancelled",'red')
              else:
                print colored("Incorrect response",'red')
            else:
              print colored("User doesn't exist",'red')
          else:
            print colored("You don't have any friends to delete",'red') 
        elif(friends_choice=='A' or friends_choice=='a'):
          friend_add=raw_input(colored("Enter user_name, which has to confirm: ",'yellow'))
          if(friend_add in dict[user_name]['Pending_friends']):
            dict[user_name]['Accepted_friends'].append(friend_add)
            dict[user_name]['Pending_friends'].remove(friend_add)
            print colored("Your friend has added to your account successfully",'yellow')
          else:
            print colored("User doesn't exist",'red')
        elif(friends_choice=='B' or friends_choice=='b'):
            print "You are out of it"
        else:
          print colored("Incorrect option",'red')   
    elif(timeline_choice=='P' or timeline_choice=='p'):
      Photos()
    elif(timeline_choice=='D' or timeline_choice=='d'):
      if(len(dict[user_name]['Diary'])==0):
        diary_selection=raw_input("You want to make diary(Y) or back(b), wrong input makes you go back: ")
        if(diary_selection=='Y' or diary_selection=='y'): 
          diary_text=raw_input(colored("Enter the text you want ot add in your notes\nNOTE: Don't use ENTER to get next line use spaces or any symbol where you want to have a new line.\n\t",'yellow'))
          dict[user_name]['Diary'].append(diary_text)
      else:
        print colored("Your dairy contains-----",'yellow')
        for i in range(len(dict[user_name]['Diary'])):
          print i,"\t",dict[user_name]['Diary'][i],'\n' 
        diary_second=raw_input(colored("Want to Add(A) a new diary or Delete(D) any of your diary or Back(b): ",'yellow'))
        if(diary_second=='A' or diary_second=='a'):
          diary_new=raw_input(colored("Write your diary:-----\n\t ",'yellow'))
          dict[user_name]['Diary'].append(diary_new)
          print "Diary has saved to your account"
        elif(diary_second=='D' or diary_second=='d'):
          diary_delete=input(colored("Enter the number of the diary you want to delete: ",'yellow'))
          dict[user_name]['Diary'].pop(diary_delete)
          print colored("The diary has been successfully deleted",'yellow')
    elif(timeline_choice=='B' or timeline_choice=='b'): 
      timeline_loop=5
    else:
      print colored("Wrong one",'red')
  



Start()

