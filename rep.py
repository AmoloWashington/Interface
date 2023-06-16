import re

def validate_form_inputs(form_data):
    errors = {}

    # Validate Name
    if not form_data.get('name'):
        errors['name'] = 'Name is required.'
    elif not re.match(r'^[a-zA-Z\s]+$', form_data['name']):
        errors['name'] = 'Invalid name. Only alphabets and spaces are allowed.'

    # Validate Email
    if not form_data.get('email'):
        errors['email'] = 'Email is required.'
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', form_data['email']):
        errors['email'] = 'Invalid email address.'

    # Validate Age
    if not form_data.get('age'):
        errors['age'] = 'Age is required.'
    elif not form_data['age'].isdigit():
        errors['age'] = 'Invalid age. Numeric value expected.'
    elif not 18 <= int(form_data['age']) <= 100:
        errors['age'] = 'Age must be between 18 and 100.'

    # Add more validation rules for other form inputs as needed...

    return errors
