## functions
import postparser
import time
import datetime

## necessary imports
from uiautomator import Device
d = Device('R58R746PGVD')
from ppadb.client import Client
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
dr = devices[0]

#loops
starting = True

#extra vars
zippy = 94536 #define before running



while True:
    
    while starting == True:
        walmart = d(text = "Walmart", resourceId = "com.sec.android.app.launcher:id/home_icon")
        signIn = d(text = "Sign in", resourceId = "com.walmart.android:id/onboarding_welcome_primary_button")
        
        clearOption = d(text = "NONE OF THE ABOVE", resourceId = "com.google.android.gms:id/cancel")
        email = d(text = "Email", className = "android.widget.EditText")
        continued = d(text = "Continue", resourceId = "com.walmart.android:id/auth_button_main")
        
        password = d(text = "Password", className = "android.widget.EditText")
        signIn2 = d(text = "Sign in", resourceId = "com.walmart.android:id/auth_button_main")
        
        zipCode = d(text = "Enter zip code", resourceId = "com.walmart.android:id/onboarding_zip_code_button")
        enterZipCode = d(text = "Enter zip code", resourceId = "com.walmart.android:id/onboarding_zip_code_textinput")
        search = d(text = "Search", resourceId = "com.walmart.android:id/onboarding_zip_code_search_button")
        
        
        if(walmart.exists == True):
            walmart.click()
            time.sleep(5)
        
        if(signIn.exists == True):
            signIn.click()
            time.sleep(5)
            
        if(clearOption.exists == True):
            clearOption.click()
            time.sleep(5)

        if(email.exists == True):
            email.click()
            time.sleep(3)
            dr.shell(f'input text "{emailUser}"')
            time.sleep(1)
            d.press.back()
            time.sleep(3)
            
        if(continued.exists == True):
            continued.click()
            time.sleep(5)
            
        if(password.exists == True):
            password.click()
            time.sleep(3)
            dr.shell(f'input text "{passUser}"')
            time.sleep(1)
            d.press.back()
            time.sleep(3)
            
        if(signIn2.exists == True):
            signIn2.click()
            time.sleep(5)
            
        if(zipCode.exists == True):
            zipCode.click()
            time.sleep(5)
            
        if(enterZipCode.exists == True):
            email.click()
            time.sleep(3)
            dr.shell(f'input text "{zippy}"')
            time.sleep(1)
            d.press.back()
            time.sleep(3)
        
        
        
        
            
        
        