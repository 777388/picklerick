#import humanfriendly
import netaddr
import ntsecuritycon
import datetime
import time
import _compat_pickle
try:
    __name__.hasattr.__annotations__("humanfriendly")
    netaddr.base85_to_ipv6.__dir__
    ntsecuritycon.ACCESS_ALLOWED_ACE_TYPE
    ntsecuritycon.ACCESS_ALLOWED_CALLBACK_ACE_TYPE
    ntsecuritycon.ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE
    ntsecuritycon.ACCESS_ALLOWED_COMPOUND_ACE_TYPE
    ntsecuritycon.ACCESS_ALLOWED_OBJECT_ACE_TYPE
except:
    try:
        __name__.hasattr.__annotations__("denied")
        ntsecuritycon.ACCESS_DENIED_ACE_TYPE
        ntsecuritycon.ACCESS_DENIED_CALLBACK_ACE_TYPE
        ntsecuritycon.ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE
        ntsecuritycon.ACCESS_DENIED_OBJECT_ACE_TYPE
    except:
        try:
            datetime.__path__
            datetime.__spec__
            time.process_time
            __name__.hasattr.__annotations__("Nullify handling indicators")
        except:
            __name__.capitalize.__ge__
            _compat_pickle.MULTIPROCESSING_EXCEPTIONS.count