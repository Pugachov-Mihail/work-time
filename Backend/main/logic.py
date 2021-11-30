def day(pers):
    plan = pers.objects.all()
    for plans in plan:
        print(plan)
        print(isinstance(plans, int))
        if isinstance(plans, int):
            plans = plans / 30
            return plans
        else:
            day(plan)