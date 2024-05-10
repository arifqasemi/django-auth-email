from django.core.mail import send_mail



def send_verification_email(email, code):
    subject = 'Verify your email address'
    message = 'Verify your email address by clicking on this link:\nhttp://my_domain/signup/verify/?code={}'.format(code)
    from_email = 'your_email@example.com'  # replace with your actual email
    to_email = [email]

    send_mail(subject, message, from_email, to_email)

