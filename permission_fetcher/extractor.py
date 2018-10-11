import re
import json
import pprint
from typing import List, Dict, Union

data = r""")]}'
4396
[["wrb.fr","xdSrCf","[[[\"Identity\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/AUs-Fih7eEfuhp-4lYGGK65UvYQ2K6qaKi0dRUipSmiac-QL94IbT-XylwOgMoaYBDLuGOz1l5Yn_K6z1NM\"]\n]\n,[[null,\"find accounts on the device\"]\n,[null,\"add or remove accounts\"]\n,[null,\"read your own contact card\"]\n]\n]\n,[\"Contacts\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/c5fJsmDZCeHY1tZmeGXL12sHi8herULd72A_egjaAHylmgM-4gLiw4CuDJSzNnK5q8yxAAy4RyxtkdYzcg\"]\n]\n,[[null,\"find accounts on the device\"]\n,[null,\"read your contacts\"]\n,[null,\"modify your contacts\"]\n]\n]\n,[\"Location\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/4rkEm_eN4F8lAtqf1avrqAQ49_IjMjRduxI5szmftCXmKzSaLsNScjM5DSGQp2qtI5R_fqj8j7aJi_G3dg\"]\n]\n,[[null,\"approximate location (network-based)\"]\n,[null,\"precise location (GPS and network-based)\"]\n]\n]\n,[\"SMS\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/T0FSi5cHSE6ZmXMZAv0tidh8XAQWi7_WqbhtZ1XfNYhLJyOfudKVtiySoaBhBku4bzpRZTnddzjL1A-D\"]\n]\n,[[null,\"read your text messages (SMS or MMS)\"]\n,[null,\"receive text messages (SMS)\"]\n]\n]\n,[\"Phone\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/QDYtvjtZon4TYi4-wkvfIqszmmJL258051XdtozjpIZVH-8zVoay1oBS9vw7lzDYYaDz48AzxmOY040lNqc\"]\n]\n,[[null,\"directly call phone numbers\"]\n,[null,\"read call log\"]\n,[null,\"read phone status and identity\"]\n,[null,\"write call log\"]\n]\n]\n,[\"Photos/Media/Files\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/pHtIujPWxciAZcfYSwlrGGq14Z984rKLMgcm9RPATLiOlbrWy-tVlelEWgED7gpktgcD1tZizVeHiO5fkw\"]\n]\n,[[null,\"read the contents of your USB storage\"]\n,[null,\"modify or delete the contents of your USB storage\"]\n]\n]\n,[\"Storage\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/aWNKQedLTpw6u6yyMjQObmuoKu67A1czWnIcvID86oAmMT02r5mNdRn6l9ZN2t2MIyH6tNy-01v7ukeQ\"]\n]\n,[[null,\"read the contents of your USB storage\"]\n,[null,\"modify or delete the contents of your USB storage\"]\n]\n]\n,[\"Camera\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/xbP_oGuJ21iG29iVh0p-UIZPzi_fYj8PMYiqDd9-LvaZ_a1tRcwp0I2-arfXvgX9YtfZTTaqwcLRWPNQM_c\"]\n]\n,[[null,\"take pictures and videos\"]\n]\n]\n,[\"Microphone\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/daUjqbSOr2QpaqXS2HQbNzYzzqN2yWGzM_7AZxwFaWLT7_kIhX95HKi_HSpjeeQDOmFMENZxJqblbu_4qg\"]\n]\n,[[null,\"record audio\"]\n]\n]\n,[\"Wi-Fi connection information\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/U-_SG8pHTsqU_IyZTGQRkVMdLaAUeq1OnKGrB06KHF1z7vkkIQK3iF0HcbfTe1RnGlh-ajnZkbphl2W3Gdk\"]\n]\n,[[null,\"view Wi-Fi connections\"]\n]\n]\n,[\"Device ID \\u0026 call information\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/l2htRLV5Mt-RZ6nroJCXy3OF_CqdntOsEetnLEjH1wC-WJWV00R5orcBWj0NMFKJVEQU6JhPYRBCKnj3_Q\"]\n]\n,[[null,\"read phone status and identity\"]\n]\n]\n,[\"SMS\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/T0FSi5cHSE6ZmXMZAv0tidh8XAQWi7_WqbhtZ1XfNYhLJyOfudKVtiySoaBhBku4bzpRZTnddzjL1A-D\"]\n]\n,[[null,\"receive text messages (SMS)\"]\n]\n]\n,[\"Phone\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/QDYtvjtZon4TYi4-wkvfIqszmmJL258051XdtozjpIZVH-8zVoay1oBS9vw7lzDYYaDz48AzxmOY040lNqc\"]\n]\n,[[null,\"read phone status and identity\"]\n]\n]\n]\n,[[\"Other\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/pkKXoPl5q7n8T0s7KREtdvUZn1PLRgx-Ox0t4tkO8af4JpgGbyAxLBTsvEKKBCjwBACQsZisSYNmHPGbBA\"]\n]\n,[[null,\"view network connections\"]\n,[null,\"create accounts and set passwords\"]\n,[null,\"pair with Bluetooth devices\"]\n,[null,\"full network access\"]\n,[null,\"change your audio settings\"]\n,[null,\"read sync settings\"]\n,[null,\"run at startup\"]\n,[null,\"draw over other apps\"]\n,[null,\"control vibration\"]\n,[null,\"prevent device from sleeping\"]\n,[null,\"toggle sync on and off\"]\n,[null,\"install shortcuts\"]\n,[null,\"uninstall shortcuts\"]\n,[null,\"read Google service configuration\"]\n]\n]\n,[\"Other\",[null,2,null,[null,null,\"https://lh3.googleusercontent.com/pkKXoPl5q7n8T0s7KREtdvUZn1PLRgx-Ox0t4tkO8af4JpgGbyAxLBTsvEKKBCjwBACQsZisSYNmHPGbBA\"]\n]\n,[[null,\"view network connections\"]\n,[null,\"full network access\"]\n,[null,\"control vibration\"]\n,[null,\"prevent device from sleeping\"]\n]\n]\n]\n,[[null,\"receive data from Internet\"]\n]\n]\n",null,null,null,"vm96le:0|ex"]
]
59
[["di",78]
,["af.httprm",79,"-7712926575713200496",133]
]
27
[["e",4,null,null,4496]
]
"""


def extract_permission_data(raw_response: str) -> List:
    raw = re.findall(r'\"(\[.*\\n)\"', raw_response)
    json_payload = raw[0].replace('\\n', '').replace('\\', '')
    return json.loads(json_payload)


BlockTyping = Dict[str, Union[str, List[str]]]


def extract_permission_blocks(permission_data: List) -> Dict[str, BlockTyping]:
    blocks = {}
    for block in permission_data:
        for line in block:
            if len(line) != 2:
                name = line[0]
                pic_url = line[1][3][2]
                permissions = [p[1] for p in line[2]]
                if name not in blocks:
                    blocks[name] = {'pic_url': pic_url, 'permissions': permissions}
                else:
                    blocks[name]['permissions'].extend(permissions)
            else:
                blocks['Other']['permissions'].append(line[1])
    return blocks


pprint.pprint(extract_permission_blocks(extract_permission_data(data)))
