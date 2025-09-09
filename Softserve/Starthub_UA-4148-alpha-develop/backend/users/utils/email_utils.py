from django.conf import settings
from django.core.mail import send_mail


def send_activation_email(token, recipient_email):
    """
    Sends an activation email with HTML and plain text versions.
    """

    activation_url = f"{settings.FRONTEND_URL}/verify-email?token={token}"

    plain_message = (
        f"Hello!\n\n"
        f"To activate your account, please click the link below:\n"
        f"{activation_url}\n\n"
        f"Token: {token}\n\n"
        "Thank you!"
    )

    html_message = f"""
    <html>
    <body>
        <p>Hello!</p>
        <p>To activate your account, click the button below:</p>
        <a href="{activation_url}" 
           style="display:inline-block; background-color:#007bff; color:#ffffff; 
                  padding:12px 24px; text-decoration:none; border-radius:6px; font-weight:bold;">
           Activate your account
        </a>
        <p>If the button does not work, copy and paste the following URL into your browser:</p>
        <p><a href="{activation_url}">{activation_url}</a></p>
        <p>Thank you!</p>
    </body>
    </html>
    """

    send_letter = send_mail(
        subject="Verify your email",
        message=plain_message,
        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@example.com"),
        recipient_list=[recipient_email],
        html_message=html_message,
        # TODO: Due to the lack of DEFAULT_FROM_EMAIL,
        # set it to True for now so that these errors do not distract
        fail_silently=True,
    )
    return send_letter == 1
