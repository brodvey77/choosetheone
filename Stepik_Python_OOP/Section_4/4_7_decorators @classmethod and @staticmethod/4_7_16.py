# import re
#
# class CaseHelper:
#     pass
#
#     @staticmethod
#     def is_snake(string: str) -> bool:
#         pattern = r'^[a-z0-9]+(_[a-z0-9]+)*$'
#         return bool(re.match(pattern, string))
#
#     @staticmethod
#     def is_upper_camel(string: str) -> bool:
#         pattern = r'^[A-Z][a-z]*([A-Z][a-z]*)*\d*$'
#         return bool(re.match(pattern, string))
#
#     @staticmethod
#     def to_snake(string: str) -> str:
#         string = re.sub(r'(?<=[a-z])([A-Z])|(?<=[A-Z])([A-Z])(?=[a-z])', r'_\1\2', string)
#         return string.lower()
#
#     @staticmethod
#     def to_upper_camel(string: str) -> str:
#         return ''.join(word.capitalize() for word in string.split('_') if word)
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# print(CaseHelper.is_snake('beegeek'))
# print(CaseHelper.is_snake('bee_geek'))
# print(CaseHelper.is_snake('Beegeek'))
# print(CaseHelper.is_snake('BeeGeek'))
# print('____________________________________________________________________')
# # TEST_2:
# print(CaseHelper.is_upper_camel('beegeek'))
# print(CaseHelper.is_upper_camel('bee_geek'))
# print(CaseHelper.is_upper_camel('Beegeek'))
# print(CaseHelper.is_upper_camel('BeeGeek'))
# print('____________________________________________________________________')
# # TEST_3:
# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))
# print('____________________________________________________________________')
# # TEST_4:
# print(CaseHelper.to_upper_camel('beegeek'))
# print(CaseHelper.to_upper_camel('bee_geek'))
# print('____________________________________________________________________')
# # TEST_5:
# cases = ['assert_equal', 'tear_down', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'its_wednesday_my_dudes']
#
# for case in cases:
#     print(CaseHelper.is_snake(case))
# print('____________________________________________________________________')
# # TEST_6:
# cases = ['assert_equal', 'tear_down', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp', 'ItsWednesdayMyDudes']
#
# for case in cases:
#     print(CaseHelper.is_upper_camel(case))
# print('____________________________________________________________________')
# # TEST_7:
# cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']
#
# for case in cases:
#     print(CaseHelper.to_snake(case))
# print('____________________________________________________________________')
# # TEST_8:
# cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']
#
# for case in cases:
#     print(CaseHelper.to_upper_camel(case))
# print('____________________________________________________________________')
# # TEST_9:
# obj = CaseHelper()
# print(type(obj.is_snake))
# print(type(obj.is_upper_camel))
# print(type(obj.to_snake))
# print(type(obj.to_upper_camel))


# https://inflection-readthedocs-io.translate.goog/en/latest/?_x_tr_sl=auto&_x_tr_tl=ru&_x_tr_hl=ru#module-inflection


import re

import inflection
from inflection import camelize


class CaseHelper:
    pass

    @staticmethod
    def is_snake(string: str) -> bool:
        pattern = r'^[a-z0-9]+(_[a-z0-9]+)*$'
        return bool(re.match(pattern, string))

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        pattern = r'^[A-Z][a-z]*([A-Z][a-z]*)*\d*$'
        return bool(re.match(pattern, string))

    @staticmethod
    def to_snake(string: str) -> str:
       return inflection.tableize(string)

    @staticmethod
    def to_upper_camel(string: str) -> str:
        return inflection.camelize(string)



# INPUT DATA:

# TEST_1:
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
print('____________________________________________________________________')
# TEST_2:
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
print('____________________________________________________________________')
# TEST_3:
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
print('____________________________________________________________________')
# TEST_4:
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
print('____________________________________________________________________')
# TEST_5:
cases = ['assert_equal', 'tear_down', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'its_wednesday_my_dudes']

for case in cases:
    print(CaseHelper.is_snake(case))
print('____________________________________________________________________')
# TEST_6:
cases = ['assert_equal', 'tear_down', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp', 'ItsWednesdayMyDudes']

for case in cases:
    print(CaseHelper.is_upper_camel(case))
print('____________________________________________________________________')
# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))
print('____________________________________________________________________')
# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))
print('____________________________________________________________________')
# TEST_9:
obj = CaseHelper()
print(type(obj.is_snake))
print(type(obj.is_upper_camel))
print(type(obj.to_snake))
print(type(obj.to_upper_camel))


print(camelize("device_type"))
