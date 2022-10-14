# ############################
# template filters
from flask import current_app as app
from markupsafe import Markup


def color_for(value: float) -> str:
	if value > 0.8:
		return 'bg-success'
	elif value > 0.6:
		return 'bg-primary'
	elif value > 0.4:
		return 'bg-warning'
	elif value > 0.2:
		return 'bg-orange'
	else:
		return 'bg-danger'


@app.template_filter()
def pretty_delta_percent(val):
	"""
		get the percent value with leading sign (+ / -)

		:param val: float value to be transformed
		:return: e.g. '+8%'
		for 0.08 or '-15%' for 0.15
	"""
	if val < 0:
		return f'{int(val * 100)}%'
	else:
		return f'+{int(val * 100)}%'


@app.template_filter()
def pretty_delta_progress(val):
	"""
		generates a html of the slider(negativ red, positive green)

		:param val:
		:return: html(safe) with positive and negative sliders
	"""
	if val > 0:
		negative_val = '0px; display: none'
		positive_val = f'{max(3, int(val * 100))}%'
	else:
		negative_val = f'{max(3, -int(val * 100))}%'
		positive_val = '0px; display: none'

	return Markup(
		'<div class="ui-progress-container">'
		'<div id="progress_bar_neg" class="ui-progress-bar ui-container" style="width: 150px;">'
		f'<div class="ui-progress-red" style="width: {negative_val}; ">&nbsp;</div><!-- .ui-progress-red -->'
		'</div><!-- #progress_bar_neg -->'
		'<div id="progress_bar_pos" class="ui-progress-bar ui-container" style="width: 150px;">'
		f'<div class="ui-progress-green" style="width: {positive_val};">&nbsp;</div><!-- .ui-progress-green -->'
		'</div><!-- #progress_bar_pos -->'
		'</div>'
	)


@app.template_filter('reverse')
def reverse_filter(s):
	"""
		reverses the list / array

		:param s: array
		:return: reversed array
	"""
	return s[::-1]
