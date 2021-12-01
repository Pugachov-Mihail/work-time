def day(pers):
    METRICS = ('metal', 'accs', 'dop', 'oss', 'setting', 'bil', 'mega', 'yota', 'tele')
    for field in METRICS:
        plan = pers.objects.filter(METRICS)
        plan[field] = 31
        return plan