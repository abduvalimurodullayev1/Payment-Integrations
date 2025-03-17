from typing import Tuple
from typing import Optional

from apps.payment.models import Providers


def get_credentials() -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    CLICK = Providers.objects.filter(provider=Providers.ProviderChoices.CLICK, is_active=True)
    CLICK_SECRET_KEY = getattr(CLICK.filter(key="CLICK_SECRET_KEY").last(), "value", None)
    CLICK_MERCHANT_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_ID").last(), "value", None)
    CLICK_MERCHANT_SERVICE_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_SERVICE_ID").last(), "value", None)
    CLICK_MERCHANT_USER_ID = getattr(CLICK.filter(key="CLICK_MERCHANT_USER_ID").last(), "value", None)
    CLICK_REDIRECT_URL = Providers.objects.filter(provider=Providers.ProviderChoices.CLICK,
                                                  is_active=True).first().value
    CLICK_IN_APP_SECRET_KEY = getattr(CLICK.filter(key="CLICK_IN_APP_SECRET_KEY").last(), "value", None)
