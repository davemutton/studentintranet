function resizeWindow()
{
	window.moveTo(0,0);
	window.resizeTo((parseInt(document.getElementsByTagName('object')[0].getAttribute('width'))+60), (parseInt(document.getElementsByTagName('object')[0].getAttribute('height'))+250));
}

window.onload = resizeWindow;
