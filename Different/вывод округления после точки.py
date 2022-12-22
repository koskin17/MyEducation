mountain = ['*', '**', '***', '****', '*****', '******']


def ski_jump(mountain):
    jump = (len(mountain) * (len(mountain) * 1.5) * 9) / 10

    if jump < 10:
        jump = "%.2f" % jump
        return "{} metres: He's crap!".format(jump)
    if 10 < jump < 25:
        jump = "%.2f" % jump
        return "{} metres: He's ok!".format(jump)
    if 25 < jump < 50:
        jump = "%.2f" % jump
        return "{} metres: He's flying!".format(jump)
    jump = "%.2f" % jump
    return "{} metres: Gold!!".format(jump)

print(ski_jump(mountain))

''' Второй вариант '''
def ski_jump(mountain):
    height = len(mountain)
    speed = height * 1.5
    jump_length = height * speed * 9 / 10
    return (
        f"{jump_length:.2f} metres: He's crap!" if jump_length < 10  else
        f"{jump_length:.2f} metres: He's ok!" if jump_length < 25 else
        f"{jump_length:.2f} metres: He's flying!" if jump_length < 50 else
        f"{jump_length:.2f} metres: Gold!!"
    )
