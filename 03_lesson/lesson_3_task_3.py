from address import Address
from mailing import Mailing


to_address = Address("456440", "Чебаркуль", "Первомайская", "19", "7")
from_address = Address("620109", "Екатеринбург", "Металлургов", "4", "102")

mailing = Mailing(to_address, from_address, cost=150, track="456456456")


print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.postal_code}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.building_number} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.building_number} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
# Распечатайте в консоль отправление в формате:
# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира>
# в <индекс>, <город>, <улица>, <дом> -<квартира>.
# Стоимость <стоимость> рублей.
