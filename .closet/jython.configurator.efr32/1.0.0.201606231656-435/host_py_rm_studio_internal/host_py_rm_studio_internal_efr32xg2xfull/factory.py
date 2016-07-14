
def RM_Factory(part_rev_name):

    if part_rev_name == 'A0':
        import revA0
        return getattr(revA0, 'RM_Device_EFR32XG2XFULL')
    elif part_rev_name is None:
        import revA0
        return getattr(revA0, 'RM_Device_EFR32XG2XFULL')
    else:
        raise ValueError("Invalid part revision {}".format(part_rev_name))

