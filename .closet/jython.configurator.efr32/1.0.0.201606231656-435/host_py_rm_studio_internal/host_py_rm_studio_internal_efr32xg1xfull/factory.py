
def RM_Factory(part_rev_name):

    if part_rev_name == 'A2':
        import revA2
        return getattr(revA2, 'RM_Device_EFR32XG1XFULL')
    elif part_rev_name == 'A3':
        import revA3
        return getattr(revA3, 'RM_Device_EFR32XG1XFULL')
    elif part_rev_name is None:
        import revA3
        return getattr(revA3, 'RM_Device_EFR32XG1XFULL')
    else:
        raise ValueError("Invalid part revision {}".format(part_rev_name))

