from .models import PersonalInfo


def personal_info(request):
	"""Expose PersonalInfo globally to all templates."""
	return {
		'personal_info': PersonalInfo.objects.first()
	}


