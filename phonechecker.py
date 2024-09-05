import phonenumbers
from phonenumbers import PhoneNumberFormat, format_number
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier


def get_number_type_description(number_type):
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        return "Số điện thoại di động"
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        return "Số điện thoại cố định"
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
        return "Số điện thoại di động hoặc cố định"
    elif number_type == phonenumbers.PhoneNumberType.VOIP:
        return "Số điện thoại VoIP"
    elif number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
        return "Số điện thoại cước phí cao"
    elif number_type == phonenumbers.PhoneNumberType.SHARED_COST:
        return "Số điện thoại chi phí chia sẻ"
    elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
        return "Số điện thoại miễn phí"
    else:
        return "Loại số điện thoại không xác định"

user_input = input("Nhập số điện thoại theo mã quốc gia (+84 cho Việt Nam): ")

try:
    
  
    phone_number = phonenumbers.parse(user_input, None)

   
    is_valid = phonenumbers.is_valid_number(phone_number)
    formatted_number = format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)
    national_format_number = format_number(phone_number, PhoneNumberFormat.NATIONAL)
    country_code = phone_number.country_code
    location = geocoder.description_for_number(phone_number, 'vi')
    time_zones = timezone.time_zones_for_number(phone_number)
    number_type = phonenumbers.number_type(phone_number)
    carrier_name = carrier.name_for_number(phone_number, 'vi')


    print(f"Số điện thoại định dạng quốc tế: {formatted_number}")
    print(f"Số điện thoại định dạng quốc gia: {national_format_number}")
    print(f"Mã quốc gia: {country_code}")
    print(f"Số điện thoại hợp lệ? {'Có' if is_valid else 'Không'}")
    print(f"Vị trí: {location}")
    print(f"Múi giờ: {', '.join(time_zones)}")
    print(f"Loại số điện thoại: {get_number_type_description(number_type)}")
    print(f"Nhà mạng: {carrier_name}")
    
    
except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f" Mã quốc gia không chính xác: {e}")
