function show(id)
{
	el = document.getElementById(id);
	if (el.style.display == 'none')
	{
		el.style.display = 'block';
		el.style.visibility = 'visible';
	} else {
		el.style.display = 'none';
		el.style.visibility = 'hidden';
	}
}