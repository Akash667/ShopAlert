// chrome.browserAction.setPopup({popup:'popup.html'});  //disable browserAction's popup

chrome.browserAction.onClicked.addListener(()=>{
    chrome.tabs.create({url:'popup.html'});
})