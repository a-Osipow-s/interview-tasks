from typing import Final
from jinja2 import Environment, TemplateSyntaxError


HYPHENS: Final = "-"
APOSTROPHE: Final = "'"


class ValidationClass:

    @staticmethod
    def validate_subject(subject):
        """Validate subject"""
        if not isinstance(subject, str):
            return False

        if not subject.strip():
            return False
        
        if not all(
            char.isalnum() or 
            char.isspace() or 
            char in (HYPHENS, APOSTROPHE) 
            for char in subject
        ):
            return False
        return True


    @staticmethod
    def validate_jinja_syntax(body_html):
        """Validate jinja syntax"""
        if not isinstance(body_html, str):
            return False

        try:
            Environment().parse(body_html)
            return True
        except TemplateSyntaxError:
            return False


def validate_template_syntax(subject, body_html):
    """Validate template subject and body_html building"""
    if ValidationClass.validate_subject(subject):
        raise ValueError("Please, check the syntax of your subject")
        
    if ValidationClass.validate_jinja_syntax(body_html):
        raise ValueError("Please, check the syntax of your message")

    return True