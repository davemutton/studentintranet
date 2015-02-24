function printPage(){
  if (window.print != null) {
    window.print(); 
    } 
  else { 
    alert("Unfortunately your browser does not support this shortcut. Please select File, then Print, from the menu");
      }
  }
function externalLinks()
{
  if (!document.getElementsByTagName) return;
  var anchors = document.getElementsByTagName("a");
  for (var i=0; i<anchors.length; i++)
  {
    var anchorElement = anchors[i];
    if (anchorElement.getAttribute("href") && (anchorElement.getAttribute("class") && anchorElement.getAttribute("class").indexOf("external") != -1 || anchorElement.getAttribute("className") && anchorElement.getAttribute("className").indexOf("external") != -1))
    {
      function newAlert()
        {
          window.alert('This will open a new window.');
        }
      try{anchorElement.addEventListener('click', newAlert, false)}
      catch(e){}
      try{anchorElement.attachEvent('onclick', newAlert)}
      catch(e){}
      anchorElement.setAttribute('target', "_blank");
      anchorElement.setAttribute('title', anchorElement.getAttribute('title') + ' (opens in new window)')
      if(anchorElement.firstChild.tagName && anchorElement.firstChild.tagName.toLowerCase() == 'img')
      {
        anchorElement.firstChild.setAttribute('alt',  anchorElement.firstChild.getAttribute('alt') + '  (opens in new window)');
      }
    }
  }
}
window.onload = externalLinks;