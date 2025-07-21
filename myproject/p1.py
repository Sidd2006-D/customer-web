import eel
# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
#eel.init('web', allowed_extensions=['.js', '.html'])

# Set web files folder
try:
    eel.init("web")

    @eel.expose             #expose this function to javascript
    def  say_hello(arg):
         print('ServerSide:',arg)
    screen_w=960
    screen_h=720

    eel.start('home.html',size=(screen_w,screen_h),port=2021)#start
    print("closed Succcessfully")
except Exception as  e:
    print('error:',e)
    
