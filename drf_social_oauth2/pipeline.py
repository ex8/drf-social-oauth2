from social_core.pipeline.partial import partial

from drf_social_oauth2.models import MultiFactorAuth


@partial
def multi_factor_auth(strategy, details, user=None, is_new=False, *args, **kwargs):
    if not user:
        # send email here
        MultiFactorAuth(
            code='123456',
            backend=kwargs['backend'].data['backend'],
            client_id=kwargs['backend'].data['client_id'],
            client_secret=kwargs['backend'].data['client_secret'],
            token=kwargs['backend'].data['token'],
        )
        print("You registration factor is: 12345")
        return {
            'redirect': 'enter_code_page',
            'steps': ['enter_code']
        }

    else:
        print('User is already authenticated')
