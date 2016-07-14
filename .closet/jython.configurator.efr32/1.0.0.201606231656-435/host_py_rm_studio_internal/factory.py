

__all__ = ['RM_Factory']

RM_PART_FAMILY_NAMES = [
    "DUMBO",
    "JUMBO",
]

def RM_Factory(part_family_name, part_rev_name=None):
    
    rm_module = __import__('host_py_rm_studio_internal')
    factory_func = None
    if part_family_name == "DUMBO":
        factory_func = getattr(
            rm_module.host_py_rm_studio_internal_efr32xg1xfull.factory,
            'RM_Factory')
    elif part_family_name == "JUMBO":
        factory_func = getattr(
            rm_module.host_py_rm_studio_internal_efr32xg2xfull.factory,
            'RM_Factory')
    else:
        raise ValueError("Invalid family name '{}'".format(part_family_name))
    
    return factory_func(part_rev_name)


