import ps_test12_custom_module
from pprint import pprint as pp

print(__name__)
print(ps_test12_custom_module.__name__)
pp(ps_test12_custom_module.ReadDir().get_files_under_directory("/etc"))
