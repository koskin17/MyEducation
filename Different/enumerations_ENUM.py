import enum


class ProgramStatus(enum.Enum):
    LOADING = 0
    WORK = 1
    CLOSE = 2


status = ProgramStatus.LOADING
print(status)
if status == ProgramStatus.LOADING:
    status = ProgramStatus.WORK

print(status)
