from django.core.exceptions import ValidationError


class ContainsLetterValidator:

    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le MDP doit contenir au moins une lettre', code='password_no_letters')

    def get_help_text(self):
        return 'Votre MDP doit contenir au moins une lettre'
