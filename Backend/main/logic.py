def day(pers):
    for plans in pers.objects.filter(gt=int):
        plan = plans / 30
        return plan
