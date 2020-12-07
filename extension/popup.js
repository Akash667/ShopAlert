'use strict';  
let GetURL = document.getElementById('GetURL');  
GetURL.onclick = function(element) {  
  getCurrentTabUrl();  
};  
  
function modifyDOM() {  
        //You can play with your DOM here or check URL against your regex  
        console.log('Tab script:');  
        console.log(document.body);  
        document.body.style.background = "blue"  
        return true;  
    }  

function getCurrentTabUrl() {  
  var queryInfo = {  
    active: true,  
    currentWindow: true  
  };    
  chrome.tabs.query(queryInfo, (tabs) => {  
    var tab = tabs[0];  
    var url = tab.url;  
    document.getElementById('url').innerHTML = url;  
  });  
}  