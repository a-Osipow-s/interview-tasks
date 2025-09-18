class ValidationClass:

    @staticmethod
    def validate_subject(subject):
        """Do something"""

    @staticmethod
    def validate_jinja_syntax(body_html):
        """Do something"""

def validate_template_syntax(subject, body_html):
    """Validate template subject and body_html building"""
    if ValidationClass.validate_subject(subject):
        raise ValueError("Please, check the syntax of your subject")
    if ValidationClass.validate_jinja_syntax(body_html):
        raise ValueError("Please, check the syntax of your message")
    return True