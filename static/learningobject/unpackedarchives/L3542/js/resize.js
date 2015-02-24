function changeWindow()
{
window.moveTo(0,0);
window.resizeTo((parseInt(document.getElementsByTagName('object')[0].getAttribute('width'))+200), (parseInt(document.getElementsByTagName('object')[0].getAttribute('height'))+160));
}
window.onload = changeWindow;
