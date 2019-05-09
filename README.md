This is a instering code!
-------------------------


```
@Override
protected void onDestroy() {
    EventBus.getDefault().unregister(this); // code
    super.onDestroy();
}
```  
