## functions
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
starting2 = True

#extra vars
zippy = 94536 #define before running



while True:
    
    while starting == True:
        print("starting")
        search = d(text = "Search Walmart", resourceId = "com.walmart.android:id/search_view")
        stringCheese = d(index = "3", resourceId = "com.walmart.android:id/product_tile_right_side_group")
        addToCart = d(text = "Add to cart", resourceId = "com.walmart.android:id/textview_add_cart_cta")
        viewCart = d(textStartsWith = "View cart", resourceId = "com.walmart.android:id/item_pac_view_cart_cta")
        cart = d(text = "Cart", className = "android.widget.TextView")
        remove = d(text = "Remove", resourceId = "com.walmart.android:id/cart_remove_button")
        
        if(search.exists == True):
            search.click()
            time.sleep(3)
            dr.shell(f'input text "String Cheese"')
            time.sleep(1)
            d.press.enter()
            time.sleep(5)
        
        if(stringCheese.exists == True):
            stringCheese.click()
            time.sleep(5)
            d.swipe(600,1100, 600, 300, steps = 3)
            time.sleep(5)
            if(addToCart.exists == True):
                addToCart.click()
                time.sleep(3)
                
        if(viewCart.exists == True):
            viewCart.click()
            time.sleep(10)
            
        if(remove.exists == True):
            remove.click()
            time.sleep(10)
                
        if(cart.exists == True):
            d.swipe(600,1100, 600, 300, steps = 3)
            d.swipe(600,300, 600, 1100, steps = 3)
            d.press.back()
            time.sleep(3)
            d.press.back()
            starting2 = True
            starting = False
            
            
    
    while starting2 == True:
        search = d(text = "Search Walmart", resourceId = "com.walmart.android:id/search_view")
        stringCheese = d(index = "3", resourceId = "com.walmart.android:id/product_tile_right_side_group")
        addToCart = d(text = "Add to cart", resourceId = "com.walmart.android:id/textview_add_cart_cta")
        viewCart = d(textContains = "View cart", resourceId = "com.walmart.android:id/item_pac_view_cart_cta")
        cart = d(text = "Cart", className = "android.widget.TextView")
        remove = d(text = "Remove", resourceId = "com.walmart.android:id/cart_remove_button")
        decline = d(text = "Decline", resourceId = "com.walmart.android:id/item_aos_decline")
        
        
        
        if(search.exists == True):
            search.click()
            time.sleep(3)
            dr.shell(f'input text "white bread"')
            time.sleep(1)
            d.press.enter()
            time.sleep(5)
        
        if(stringCheese.exists == True):
            stringCheese.click()
            time.sleep(5)
            d.swipe(600,1100, 600, 300, steps = 3)
            time.sleep(5)
            if(addToCart.exists == True):
                addToCart.click()
                time.sleep(3)
                
        if(decline.exists == True):
            decline.click()
            time.sleep(3)
                
        if(viewCart.exists == True):
            viewCart.click()
            time.sleep(10)
            
        if(remove.exists == True):
            remove.click()
            time.sleep(10)
                
        if(cart.exists == True):
            d.swipe(600,1100, 600, 300, steps = 3)
            d.swipe(600,300, 600, 1100, steps = 3)
            d.press.back()
            time.sleep(3)
            d.press.back()
            starting = True
            starting2 = False
        