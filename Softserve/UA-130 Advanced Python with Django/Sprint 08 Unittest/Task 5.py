# Create class Worker with fields name and salary. If salary negative raise ValueError

# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:

# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. Don`t use assertRaises in tests.